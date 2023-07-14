import pytest
import requests
import requests_mock

def test_read_users_endpoint_with_invalid_credentials(mocker):
    url = 'https://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'qwerty'
    }

    with requests_mock.Mocker() as mock:
        mock.get(url, status_code=200, text='')

        response = requests.get(url, params=params, verify=False)

        assert response.status_code == 200
        assert response.text == ''

def test_read_users_endpoint_with_valid_credentials(mocker):
    url = 'https://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'admin'
    }

    with requests_mock.Mocker() as mock:
        mock.get(url, status_code=401, text='')

        response = requests.get(url, params=params, verify=False)

        assert response.status_code == 401
        assert response.text == ''
