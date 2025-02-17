import pytest
import requests
import logging
from src.network_request_logger import log_network_request_response_time

def test_successful_get_request(caplog):
    caplog.set_level(logging.INFO)
    
    # Test a known working URL
    response = log_network_request_response_time('https://httpbin.org/get')
    
    # Check response
    assert response.status_code == 200
    
    # Check logging
    assert len(caplog.records) > 0
    log_record = caplog.records[0]
    assert 'Request to https://httpbin.org/get using GET method completed' in log_record.message
    assert 'ms (Status Code: 200)' in log_record.message

def test_invalid_method():
    with pytest.raises(ValueError, match="Invalid HTTP method"):
        log_network_request_response_time('https://httpbin.org/get', method='INVALID')

def test_network_error(mocker):
    # Simulate a network error
    mocker.patch('requests.request', side_effect=requests.RequestException("Network error"))
    
    with pytest.raises(requests.RequestException, match="Network error"):
        log_network_request_response_time('https://non-existent-url.com')

def test_different_methods():
    # Test various HTTP methods
    methods = ['POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']
    
    for method in methods:
        response = log_network_request_response_time('https://httpbin.org/' + method.lower(), method=method)
        assert response.status_code in [200, 405]  # 200 or method not allowed is acceptable