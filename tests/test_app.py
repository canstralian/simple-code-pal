import pytest
from flask import Flask

from templates.app-py import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the index route to ensure it returns a 200 status code."""
    response = client.get('/')
    assert response.status_code == 200

def test_generate_route_no_description(client):
    """Test the generate route to ensure it returns a 400 status code when no description is provided."""
    response = client.post('/generate', json={})
    assert response.status_code == 400

def test_generate_route_no_api_key(client, monkeypatch):
    """Test the generate route to ensure it returns a 500 status code when the API key is not configured."""
    monkeypatch.setattr('templates.app-py.CODEPAL_API_KEY', None)
    response = client.post('/generate', json={'description': 'Test description'})
    assert response.status_code == 500

def test_generate_route_valid_description(client, monkeypatch):
    """Test the generate route to ensure it returns a 200 status code and generated code when a valid description is provided."""
    monkeypatch.setattr('templates.app-py.CODEPAL_API_KEY', 'test_api_key')
    monkeypatch.setattr('templates.app-py.requests.post', lambda *args, **kwargs: MockResponse())
    response = client.post('/generate', json={'description': 'Test description'})
    assert response.status_code == 200
    assert 'code' in response.get_json()

class MockResponse:
    @staticmethod
    def json():
        return {'code': 'Generated code'}
    @staticmethod
    def raise_for_status():
        pass
