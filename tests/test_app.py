import json
import pytest
from unittest.mock import patch, MagicMock

# Import the Flask app
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from templates.app_py import app

@pytest.fixture
def client():
    """Create a test client for the app."""
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the index route returns the correct template."""
    response = client.get('/')
    assert response.status_code == 200

def test_generate_empty_description(client):
    """Test generate route with empty description."""
    response = client.post('/generate', 
                          json={'description': ''},
                          content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

@patch('templates.app_py.CODEPAL_API_KEY', None)
def test_generate_missing_api_key(client):
    """Test generate route with missing API key."""
    response = client.post('/generate',
                          json={'description': 'test description'},
                          content_type='application/json')
    assert response.status_code == 500
    data = json.loads(response.data)
    assert 'error' in data

@patch('templates.app_py.requests.post')
def test_generate_successful_response(mock_post, client):
    """Test generate route with successful API response."""
    # Mock the API response
    mock_response = MagicMock()
    mock_response.json.return_value = {'code': 'print("Hello World")'}
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    response = client.post('/generate',
                          json={'description': 'Print hello world'},
                          content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['code'] == 'print("Hello World")'

@patch('templates.app_py.requests.post')
def test_generate_api_error(mock_post, client):
    """Test generate route with API error."""
    # Mock a request exception
    mock_post.side_effect = requests.RequestException("API Error")

    response = client.post('/generate',
                          json={'description': 'test description'},
                          content_type='application/json')
    
    assert response.status_code == 500
    data = json.loads(response.data)
    assert 'error' in data