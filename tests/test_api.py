import requests

def test_get_contacts():
    response = requests.get("http://localhost:8000/contacts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
