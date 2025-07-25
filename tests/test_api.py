import requests
import time

def wait_for_api(url, timeout=30):
    for _ in range(timeout):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)
    return False

def test_get_contacts():
    api_url = "http://localhost:8000/contacts/"
    assert wait_for_api(api_url), f"La API no respondió en {api_url}"
    response = requests.get(api_url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_api_health():
    url = "http://localhost:8000/contacts/"
    for _ in range(30):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    assert False, "La API no respondió a tiempo en /contacts/"

def test_swagger_docs_available():
    url = "http://localhost:8000/docs"
    for _ in range(30):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    else:
        raise TimeoutError("Swagger docs no están disponibles")

    assert "<title>Swagger UI</title>" in response.text
