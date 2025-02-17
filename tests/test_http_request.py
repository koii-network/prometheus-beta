import pytest
import requests
import responses
from src.http_request import send_http_get_request

def test_successful_get_request():
    """Test a successful HTTP GET request."""
    with responses.RequestsMock() as rsps:
        test_url = 'https://api.example.com/test'
        test_response_data = {'key': 'value'}
        
        rsps.add(
            responses.GET, 
            test_url, 
            json=test_response_data, 
            status=200,
            headers={'content-type': 'application/json'}
        )
        
        result = send_http_get_request(test_url)
        
        assert result['status_code'] == 200
        assert result['json'] == test_response_data

def test_get_request_with_headers():
    """Test GET request with custom headers."""
    with responses.RequestsMock() as rsps:
        test_url = 'https://api.example.com/test'
        test_headers = {'Authorization': 'Bearer token123'}
        
        rsps.add(responses.GET, test_url, status=200)
        
        result = send_http_get_request(test_url, headers=test_headers)
        
        assert result['status_code'] == 200

def test_get_request_with_params():
    """Test GET request with query parameters."""
    with responses.RequestsMock() as rsps:
        test_url = 'https://api.example.com/test'
        test_params = {'key1': 'value1', 'key2': 'value2'}
        
        rsps.add(responses.GET, test_url, status=200)
        
        result = send_http_get_request(test_url, params=test_params)
        
        assert result['status_code'] == 200

def test_request_exception():
    """Test handling of request exceptions."""
    with responses.RequestsMock() as rsps:
        test_url = 'https://api.example.com/error'
        
        rsps.add(responses.GET, test_url, body=requests.exceptions.RequestException('Network error'))
        
        with pytest.raises(requests.RequestException):
            send_http_get_request(test_url)

def test_bad_status_code():
    """Test handling of bad HTTP status codes."""
    with responses.RequestsMock() as rsps:
        test_url = 'https://api.example.com/notfound'
        
        rsps.add(responses.GET, test_url, status=404)
        
        with pytest.raises(requests.HTTPError):
            send_http_get_request(test_url)