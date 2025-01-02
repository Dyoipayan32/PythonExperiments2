import pytest
from py_fixture1 import setup_fixture_auto_use
from unittest.mock import patch, Mock
from make_http_requests import fetch_data_from_api, send_data_to_api


@pytest.mark.usefixtures("setup_fixture_auto_use")
class TestFix03:
    def test_fetch_data_from_api(self):
        # Mock the requests.get function
        with patch('requests.get') as mock_get:
            # Set up the mock response
            mock_response = {'key': 'value'}
            mock_get.return_value.json.return_value = mock_response

            # Call the function with a mock URL
            result = fetch_data_from_api('http://example.com/api')

            # Assertions
            assert result == mock_response
            mock_get.assert_called_once_with('http://example.com/api')

    def test_send_data_to_api(self):
        # Mock the requests.post function
        with patch('requests.post') as mock_post:
            # Set up the mock response
            mock_response = Mock(status_code=201)
            mock_post.return_value = mock_response

            # Call the function with mock data
            result = send_data_to_api('http://example.com/api', {'key': 'value'})

            # Assertions
            assert result == 201
            mock_post.assert_called_once_with('http://example.com/api', json={'key': 'value'})


if __name__ == '__main__':
    pass
else:
    fix_obj = TestFix03()
    print("printing inside main.")
    # print(fix_obj.get_value())
    print(dir(fix_obj))
