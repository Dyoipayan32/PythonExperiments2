import os
import pytest


def test_01():
    os.system('run.bat')
    var = os.getenv('MY_ENV_VAR')
    print(var)


@pytest.fixture(scope='session')
def getUserNamePasswordEnvVar():
    username = os.getenv('username')
    password = os.getenv('password')

    return username, password


@pytest.fixture
def dummy_login(getUserNamePasswordEnvVar):
    userNameVar = getUserNamePasswordEnvVar[0]
    passWordVar = getUserNamePasswordEnvVar[1]

    # Mimic a login process
    def authenticate(username, password):
        if username == userNameVar and password == passWordVar:
            return True
        return False

    return authenticate


def test_login_successful(dummy_login):
    result = dummy_login("expected_user", "correct_secret")
    assert result == True, "The login should be successful for correct credentials"
