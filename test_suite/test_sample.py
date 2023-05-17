import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Language Detection App</title>' in response.data

def test_predict(client):
    response = client.post('/predict', data={'text': 'Hello world!'})
    assert response.status_code == 200
    assert b'The entered text is in English' in response.data

def test_translate(client):
    response = client.post('/translate', data={'text': 'Hello world!', 'lang': 'es'})
    assert response.status_code == 200
    assert b'Hola Mundo!' in response.data

def test_invalid_language(client):
    response = client.post('/translate', data={'text': 'Hello world!', 'lang': 'invalid'})
    assert response.status_code == 200
    assert b'The language you entered is not supported' in response.data

def test_empty_input(client):
    response = client.post('/predict', data={'text': ''})
    assert response.status_code == 200
    assert b'Please enter some text' in response.data

def test_invalid_input(client):
    response = client.post('/predict', data={'text': '1 2 3'})
    assert response.status_code == 200
    assert b'The entered text is in Invalid' in response.data