import json.decoder
from typing import Optional

import jwt as jwt
from requests import Session
import time
import os
import json as jsonLib
import platform
import pytest
import uuid
from datetime import datetime
import psycopg2
from psycopg2._psycopg import ProgrammingError


class ResponseError(Exception):
    """Basic Exception for when a request returns an error."""

    def __init__(self, response):
        self.response = response
        try:
            content = str(jsonLib.loads(response.content)) if response.content else None
            super(ResponseError, self).__init__(content)
        except json.decoder.JSONDecodeError:
            print(response)


class Endpoints:
    GENERATE_INTERNAL_TOKEN = "auth/api/v1/Auth/Token"
    GET_O_SERIES_CREDENTIALS = 'qaagent/api/v1/Tenant'
    GET_O_SERIES_AUTH_TOKEN = 'identity/connect/token'
    USERS = "users"


class ValidationMessages:
    SUCCESS = "Valid UUID"
    FORMAT_ERROR = "Invalid UUID format"
    VERSION_ERROR = "Invalid UUID version"


class ApiClient(Session):

    def __init__(self):

        super(ApiClient, self).__init__()
        self.env = None
        self.default_env = self.env

    def get_env_variable(self, key: str, default: Optional[str] = None) -> str:
        """
        Returns environment variable, or raise an KeyError if such variable or default variable is not present in env.
        :param key: str, required, variable name.
        :param default: str, optional, default variable name to get from env, if key is not found.
        :raise Exception: in case of both arguments are missed, or none of the arguments are present in environment.
        :return: str, environment variable
        """
        if key is not None:
            envVar = os.getenv(key)
        elif default is not None:
            envVar = os.getenv(default)
        else:
            raise Exception("Key or Default Key should be provided")
        if envVar is None:
            raise Exception("There are no variable with provided name stored in environment")
        return envVar

    def get_username(self):
        return os.getenv('TESTER_USERNAME').split('@')[0]

    def get_admin_username(self):
        return os.getenv('ADMIN_USERNAME')

    def get_unique_uuid(self):
        """Returns a unique 36 character alphanumeric string in format 00000000-0000-0000-0000-000000000000 """

        return str(uuid.uuid4())

    def get_mif_month_from_database(self, auto_commit: bool = False):
        """Returns the MifMonth as a date object"""
        dbName = os.getenv("DB_NAME")
        sql = f'select mifmonth from {dbName}.dbo.databasereleaseinfo'
        conn = psycopg2.connect(
            database=dbName,
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"))
        conn.autocommit = auto_commit
        cursor = conn.cursor()
        cursor.execute(sql)
        try:
            resp = cursor.fetchall()
            cursor.close()
            mifMonth = datetime.date(resp[0][0])
            return mifMonth
        except ProgrammingError as e:
            return

    def get(self, urlPath, accept='*/*', **kwargs):
        """
        Returns data as a dictionary.
        """
        self.response = None
        _url = self._build_url(urlPath)
        headers = self._set_headers(urlPath)
        if not headers:
            self.response = super(ApiClient, self).get(_url, **kwargs)
        else:
            self.response = super(ApiClient, self).get(_url, headers=headers, **kwargs)
        return self._verify_response(self.response)

    def post(self, urlPath, **kwargs):
        _url = self._build_url(urlPath)
        headers = self._set_headers(urlPath)
        if not headers:
            r = super(ApiClient, self).post(_url, **kwargs)
        else:
            r = super(ApiClient, self).post(_url, headers=headers, **kwargs)
        return self._verify_response(r)

    def put(self, urlPath, **kwargs):
        _url = self._build_url(urlPath)
        headers = self._set_headers(urlPath)
        if not headers:
            r = super(ApiClient, self).put(_url, **kwargs)
        else:
            r = super(ApiClient, self).put(_url, headers=headers, **kwargs)
        return self._verify_response(r)

    def patch(self, urlPath, **kwargs):
        _url = self._build_url(urlPath)
        headers = self._set_headers(urlPath)
        if not headers:
            r = super(ApiClient, self).patch(_url, **kwargs)
        else:
            r = super(ApiClient, self).patch(_url, headers=headers, **kwargs)
        return self._verify_response(r)

    def delete(self, urlPath, **kwargs):
        _url = self._build_url(urlPath)
        headers = self._set_headers(urlPath)
        if not headers:
            r = super(ApiClient, self).delete(_url, **kwargs)
        else:
            r = super(ApiClient, self).delete(_url, headers=headers, **kwargs)
        return self._verify_response(r)

    def run_verify_status_code(self, expectedStatusCode, component, *args, **kwargs):
        """
        Will run the given component with the given arguments. Will then check to see if the returned status code matches the expected.
        Should be used for user access testing.
        Example: api.client.run_expect_error('Error user is locked.', api.client.login, platformadmin, password)
        :param expectedStatusCode: The Status code expected.
        :param component: The name of the component to run
        :param args: The list of arguments that the component is expecting. See above for an example.
        """
        try:
            component(*args, **kwargs)
            assert int(
                expectedStatusCode) == 200, f"Expected status code of {expectedStatusCode} did not match the actual status code of 200"
        except ResponseError as e:
            assert int(
                expectedStatusCode) == e.response.status_code, f"Expected status code of {expectedStatusCode} did not match the actual status code of {e.response.status_code}"

    def run_expect_error(self, expectedError, component, *args, **kwargs):
        """
        Will run the given component with the given arguments. Will then check to see if the returned error matches the expected error.
        Should be used for negative testing.

        Example: api.client.run_expect_error('Error user is locked.', api.client.login, platformadmin, password)

        :param expectedError: The expected error message. Case sensitive.
        :param component: The name of the component to run
        :param args: The list of arguments that the component is expecting. See above for an example.
        """
        try:
            component(*args, **kwargs)
            assert False, "No error was returned."
        except Exception as e:
            if expectedError == "":
                assert str(
                    e) == 'None', 'Actual and expected error message does not match. Expected: "{e}" Actual: "{a}"'.format(
                    e=expectedError, a=str(e))
            else:
                with pytest.assume:
                    assert expectedError in str(
                        e), 'Actual and expected error message does not match. Expected: "{e}" Actual: "{a}"'.format(
                        e=expectedError, a=str(e))

    def is_valid_uuid4(self, uuidValue: str):
        """
        method will validate if given string is valid uuid4
        :param uuidValue: input string to be validated
        :return: String validation message if given string is valid uuid and String error message if given string
        is invalid uuid
        """

        try:
            parsed_uuid = uuid.UUID(uuidValue, version=4)
        except ValueError:
            return ValidationMessages.FORMAT_ERROR
        if str(parsed_uuid) == uuidValue and parsed_uuid.version == 4:
            return ValidationMessages.SUCCESS
        else:
            return ValidationMessages.VERSION_ERROR

    #######################
    # Internal Components #
    #######################

    def _set_headers(self, url):
        header = {}
        return header

    def _verify_response(self, response):
        if not response.ok:
            try:
                print(f"response headers : {response.headers}")
            except KeyError:
                print(
                    "There was some internal error.")
            raise ResponseError(response)
        try:
            return jsonLib.loads(response.text)
        except ValueError:
            return response.text

    def _add_header(self, header):
        """ adds header to all future requests
        :param header: Dictionary with header items"""
        self.headers.update(header)

    def _build_url(self, urlPath):
        """
        Build the complete URL using the current base URL and the provided path.

        :param urlPath: str, required, path to be appended to the base URL.
        :return: str, complete URL.
        """
        # if self.env is not None:
        #     base_url = self.get_env_variable(self.env)
        # else:
        #     base_url = self.get_env_variable(self.default_env)
        base_url = "https://jsonplaceholder.typicode.com"

        return base_url + urlPath

    def _clear_header(self):
        """Clear and reset headers for all future requests."""
        self.headers = {}

    def _decode_internal_user_token(self, token) -> dict:
        """
        Decode an internal user token and return the information encoded within.
        :return: A dictionary containing decoded information from the user token.
        """
        return jwt.decode(token, options={"verify_signature": False})
