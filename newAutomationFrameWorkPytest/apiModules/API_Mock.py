from newAutomationFrameWorkPytest.apiModules.client import ApiClient


class APIMock:
    def __init__(self, client: ApiClient):
        self.client = client

    def fetch_data_from_api(self, endpoint):
        return self.client.get(endpoint)

    def send_data_to_api(self, endpoint, data):
        return self.client.post(endpoint, json=data)
