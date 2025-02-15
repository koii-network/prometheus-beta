import pytest
import requests
import responses
from src.http_post_request import send_http_post_request

def test_successful_post_request():
    # Mock a successful POST request
    with responses.RequestsMock() as rsps:
        test_url = 'https://example.com/api'
        test_data = {'key': 'value'}
        test_response_data = {'result': 'success'}
        
        rsps.add(
            responses.POST, 
            test_url, 
            json=test_response_data, 
            status=200
        )
        
        result = send_http_post_request(test_url, data=test_data)
        
        assert result['status_code'] == 200
        assert result['json'] == test_response_data

def test_post_request_with_custom_headers():
    # Test sending request with custom headers
    with responses.RequestsMock() as rsps:
        test_url = 'https://example.com/api'
        test_headers = {'Authorization': 'Bearer token123'}
        
        rsps.add(
            responses.POST, 
            test_url, 
            json={}, 
            status=200
        )
        
        result = send_http_post_request(test_url, headers=test_headers)
        assert result['status_code'] == 200

def test_request_timeout():
    # Test request timeout handling
    with pytest.raises(Exception):
        send_http_post_request('http://nonexistent-url.com', timeout=1)

def test_error_response():
    # Mock a server error response
    with responses.RequestsMock() as rsps:
        test_url = 'https://example.com/api'
        
        rsps.add(
            responses.POST, 
            test_url, 
            status=500,
            json={'error': 'Internal Server Error'}
        )
        
        result = send_http_post_request(test_url)
        assert result['status_code'] == 500