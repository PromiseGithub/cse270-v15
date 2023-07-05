import requests

def test_endpoint():
    url = "http://127.0.0.1:8000/users/"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    response = requests.get(url, params=params)

    # Verify the response
    assert response.status_code == 200


def test_endpoints():
    url = "http://127.0.0.1:8000/users/"
    params = {
        "username": "admin",
        "password": "admin"
    }

    response = requests.get(url, params=params)

    # Verify the response
    assert response.status_code == 401
    # assert response.json() == {"message": "Success"}

