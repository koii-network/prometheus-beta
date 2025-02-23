import pytest
import requests
import responses
from src.http_request import send_http_get_request

@pytest.fixture
def mock_successful_response():
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET, 
            'https://example.com', 
            json={'key': 'value'}, 
            status=200,
            headers={'content-type': 'application/json'}
        )
        yield rsps

def test_successful_json_request(mock_successful_response):
    """Test successful JSON GET request."""
    result = send_http_get_request('https://example.com')
    
    assert result['status_code'] == 200
    assert result['json'] == {'key': 'value'}
    assert 'text' in result
    assert 'headers' in result

def test_request_with_headers(mock_successful_response):
    """Test sending request with custom headers."""
    headers = {'Authorization': 'Bearer test_token'}
    result = send_http_get_request('https://example.com', headers=headers)
    
    assert result['status_code'] == 200

def test_empty_url_raises_error():
    """Test that empty URL raises ValueError."""
    with pytest.raises(ValueError, match="URL cannot be empty"):
        send_http_get_request('')

def test_invalid_url_raises_error():
    """Test that invalid URL raises RuntimeError."""
    with pytest.raises(RuntimeError):
        send_http_get_request('https://non-existent-domain-xyz123.com')

def test_request_timeout():
    """Test request timeout behavior."""
    with pytest.raises(RuntimeError):
        send_http_get_request('https://example.com', timeout=0.001)

@responses.activate
def test_non_json_response():
    """Test response with non-JSON content."""
    responses.add(
        responses.GET, 
        'https://example.com', 
        body='Plain text response', 
        status=200,
        headers={'content-type': 'text/plain'}
    )
    
    result = send_http_get_request('https://example.com')
    
    assert result['status_code'] == 200
    assert result['json'] is None
    assert result['text'] == 'Plain text response'