import pytest
import requests
from src.http_request import send_get_request

def test_send_get_request_success(requests_mock):
    """Test successful GET request"""
    mock_url = 'https://example.com/api'
    mock_response = {'key': 'value'}
    
    requests_mock.get(mock_url, json=mock_response, status_code=200)
    
    result = send_get_request(mock_url)
    
    assert result['status_code'] == 200
    assert result['json'] == mock_response

def test_send_get_request_with_headers(requests_mock):
    """Test GET request with custom headers"""
    mock_url = 'https://example.com/api'
    mock_headers = {'Authorization': 'Bearer token123'}
    
    requests_mock.get(mock_url, json={}, status_code=200)
    
    result = send_get_request(mock_url, headers=mock_headers)
    
    assert result['status_code'] == 200

def test_send_get_request_with_params(requests_mock):
    """Test GET request with query parameters"""
    mock_url = 'https://example.com/api'
    mock_params = {'page': 1, 'limit': 10}
    
    requests_mock.get(mock_url, json={}, status_code=200)
    
    result = send_get_request(mock_url, params=mock_params)
    
    assert result['status_code'] == 200

def test_send_get_request_invalid_url():
    """Test handling of invalid URL"""
    with pytest.raises(ValueError):
        send_get_request("")
    
    with pytest.raises(ValueError):
        send_get_request(None)

def test_send_get_request_network_error(requests_mock):
    """Test network-related request errors"""
    mock_url = 'https://example.com/api'
    
    requests_mock.get(mock_url, exc=requests.exceptions.ConnectTimeout)
    
    with pytest.raises(RuntimeError):
        send_get_request(mock_url)