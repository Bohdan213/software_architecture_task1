import uuid
import requests


def generate_uuid():
    return str(uuid.uuid4())


def perform_get_request(url, params, headers=None):
    if headers is None:
        headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers, params=params)
    return response


def perform_post_request(url, data, headers=None):
    if headers is None:
        headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data)
    return response
