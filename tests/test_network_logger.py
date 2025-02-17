import pytest
import requests
import time
from src.network_logger import log_network_request_time

def test_log_network_request_time(mocker):
    # Mock the requests.request method to simulate a successful request
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mocker.patch('requests.request', return_value=mock_response)
    
    # Mock time.time to control timing
    mock_time = mocker.patch('time.time', side_effect=[0, 0.5])
    
    # Test successful request
    result = log_network_request_time('https://example.com')
    
    assert result['url'] == 'https://example.com'
    assert result['method'] == 'GET'
    assert result['status_code'] == 200
    assert result['response_time_ms'] == 500  # 0.5 seconds = 500 ms

def test_log_network_request_with_custom_method():
    # Use a real request to test actual behavior (consider mocking in production)
    result = log_network_request_time('https://www.google.com', method='HEAD')
    
    assert result['url'] == 'https://www.google.com'
    assert result['method'] == 'HEAD'
    assert result['status_code'] == 200
    assert 'response_time_ms' in result

def test_network_request_error(mocker):
    # Simulate a network request exception
    mocker.patch('requests.request', side_effect=requests.RequestException)
    
    with pytest.raises(requests.RequestException):
        log_network_request_time('https://nonexistent-url.xyz')

def test_request_timeout(mocker):
    # Simulate a timeout scenario
    mocker.patch('requests.request', side_effect=requests.Timeout)
    
    with pytest.raises(requests.Timeout):
        log_network_request_time('https://example.com', timeout=1)