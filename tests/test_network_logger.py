import pytest
import requests
import responses
from src.network_logger import log_network_request_time

def test_log_network_request_time_get_success():
    # Mock a successful GET request
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, 'https://example.com', status=200, body='OK')
        
        result = log_network_request_time('https://example.com')
        
        assert result['url'] == 'https://example.com'
        assert result['method'] == 'GET'
        assert result['status_code'] == 200
        assert result['success'] is True
        assert 'response_time' in result
        assert result['response_time'] >= 0

def test_log_network_request_time_post_success():
    # Mock a successful POST request
    with responses.RequestsMock() as rsps:
        rsps.add(responses.POST, 'https://example.com/post', status=201, body='Created')
        
        result = log_network_request_time('https://example.com/post', method='POST')
        
        assert result['url'] == 'https://example.com/post'
        assert result['method'] == 'POST'
        assert result['status_code'] == 201
        assert result['success'] is True

def test_log_network_request_time_request_error():
    # Simulate a request that fails
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, 'https://nonexistent.example.com', body=requests.exceptions.ConnectionError())
        
        with pytest.raises(requests.exceptions.RequestException):
            log_network_request_time('https://nonexistent.example.com')

def test_log_network_request_time_unsupported_method():
    # Test unsupported HTTP method
    with pytest.raises(ValueError):
        log_network_request_time('https://example.com', method='PATCH')

def test_log_network_request_time_timeout():
    # Test timeout behavior
    with responses.RequestsMock() as rsps:
        # Configure a timeout
        rsps.add(responses.GET, 'https://example.com', body=requests.exceptions.Timeout())
        
        with pytest.raises(requests.exceptions.Timeout):
            log_network_request_time('https://example.com', timeout=1)