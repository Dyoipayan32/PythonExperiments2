import requests


def fetch_data_from_api(url):
    response = requests.get(url)
    return response.json()


def send_data_to_api(url, data):
    response = requests.post(url, json=data)
    return response.status_code
