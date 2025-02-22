import pytest
import requests
import time
from unittest.mock import patch
from src.network_logger import log_network_request_time

def test_log_network_request_time_success():
    # Test a successful network request
    with patch('requests.request') as mock_request:
        # Create a mock response
        mock_response = mock_request.return_value
        mock_response.status_code = 200
        
        result = log_network_request_time('https://example.com')
        
        assert 'request_details' in result
        assert 'response_time' in result
        assert 'status_code' in result
        assert result['status_code'] == 200
        assert result['request_details']['url'] == 'https://example.com'

def test_log_network_request_time_custom_method():
    # Test with a custom HTTP method
    with patch('requests.request') as mock_request:
        mock_response = mock_request.return_value
        mock_response.status_code = 201
        
        result = log_network_request_time('https://example.com', method='POST')
        
        assert result['request_details']['method'] == 'POST'

def test_log_network_request_time_with_headers():
    # Test with custom headers
    headers = {'Authorization': 'Bearer token123'}
    with patch('requests.request') as mock_request:
        mock_response = mock_request.return_value
        mock_response.status_code = 200
        
        result = log_network_request_time('https://example.com', headers=headers)
        
        assert result['request_details']['headers'] == headers

def test_log_network_request_time_request_exception():
    # Test error handling
    with patch('requests.request', side_effect=requests.RequestException('Connection error')):
        with pytest.raises(requests.RequestException):
            log_network_request_time('https://example.com')

def test_log_network_request_time_response_time_accuracy():
    # Test that response time is calculated correctly
    with patch('requests.request') as mock_request:
        mock_response = mock_request.return_value
        mock_response.status_code = 200
        
        with patch('time.time', side_effect=[0, 1.5]):  # Simulate 1.5 seconds elapsed
            result = log_network_request_time('https://example.com')
            
            assert abs(result['response_time'] - 1.5) < 0.001