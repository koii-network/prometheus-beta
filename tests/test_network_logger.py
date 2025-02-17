import pytest
import requests
import time
from unittest.mock import patch
from src.network_logger import log_network_request_response_time

class MockResponse:
    def __init__(self, status_code=200, text='Test Response', headers=None):
        self.status_code = status_code
        self.text = text
        self.headers = headers or {}

def test_log_network_request_basic():
    # Mocking requests.request to avoid actual network calls
    with patch('requests.request') as mock_request:
        mock_request.return_value = MockResponse()
        
        with patch('time.time', side_effect=[0, 0.5]):  # Simulate 0.5 seconds response time
            result = log_network_request_response_time('https://example.com')
            
            assert result['url'] == 'https://example.com'
            assert result['method'] == 'GET'
            assert result['status_code'] == 200
            assert result['response_time'] == 0.5

def test_log_network_request_custom_method():
    with patch('requests.request') as mock_request:
        mock_request.return_value = MockResponse()
        
        result = log_network_request_response_time(
            'https://example.com', 
            method='POST', 
            headers={'Content-Type': 'application/json'}
        )
        
        assert result['method'] == 'POST'
        assert len(result['headers']) >= 0

def test_log_network_request_exception():
    with patch('requests.request', side_effect=requests.RequestException("Network Error")):
        with pytest.raises(requests.RequestException):
            log_network_request_response_time('https://invalid-url.com')

def test_log_network_request_timeout():
    with patch('requests.request', side_effect=requests.Timeout("Request Timed Out")):
        with pytest.raises(requests.Timeout):
            log_network_request_response_time('https://example.com', timeout=0.1)

def test_log_network_request_params():
    with patch('requests.request') as mock_request:
        mock_request.return_value = MockResponse()
        
        result = log_network_request_response_time(
            'https://example.com', 
            params={'key1': 'value1', 'key2': 'value2'}
        )
        
        assert result['url'] == 'https://example.com'
        mock_request.assert_called_once()