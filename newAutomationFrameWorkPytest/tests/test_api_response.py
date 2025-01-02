from newAutomationFrameWorkPytest.ControllerAPI import ControllerAPI
# from newAutomationFrameWorkPytest.PageObjectsUI import PageObjectsUI


def test_api_validate_mock_response(api: ControllerAPI):
    endpoint = "/todos/?id=2"
    api.apiMock.fetch_data_from_api(endpoint)

