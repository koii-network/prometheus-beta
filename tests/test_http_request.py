import pytest
import requests
from src.http_request import send_get_request

def test_send_get_request_success(monkeypatch):
    """Test successful GET request"""
    mock_url = 'https://example.com/api'
    mock_response = {'key': 'value'}
    
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.headers = {'Content-Type': 'application/json'}
            self.text = str(mock_response)
        
        def json(self):
            return mock_response
        
        def raise_for_status(self):
            pass
    
    def mock_get(*args, **kwargs):
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    result = send_get_request(mock_url)
    
    assert result['status_code'] == 200
    assert result['json'] == mock_response

def test_send_get_request_with_headers(monkeypatch):
    """Test GET request with custom headers"""
    mock_url = 'https://example.com/api'
    mock_headers = {'Authorization': 'Bearer token123'}
    
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.headers = {}
            self.text = ''
        
        def json(self):
            return {}
        
        def raise_for_status(self):
            pass
    
    def mock_get(*args, **kwargs):
        assert kwargs['headers'] == mock_headers
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    result = send_get_request(mock_url, headers=mock_headers)
    assert result['status_code'] == 200

def test_send_get_request_with_params(monkeypatch):
    """Test GET request with query parameters"""
    mock_url = 'https://example.com/api'
    mock_params = {'page': 1, 'limit': 10}
    
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.headers = {}
            self.text = ''
        
        def json(self):
            return {}
        
        def raise_for_status(self):
            pass
    
    def mock_get(*args, **kwargs):
        assert kwargs['params'] == mock_params
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    result = send_get_request(mock_url, params=mock_params)
    assert result['status_code'] == 200

def test_send_get_request_invalid_url():
    """Test handling of invalid URL"""
    with pytest.raises(ValueError):
        send_get_request("")
    
    with pytest.raises(ValueError):
        send_get_request(None)

def test_send_get_request_network_error(monkeypatch):
    """Test network-related request errors"""
    mock_url = 'https://example.com/api'
    
    def mock_get(*args, **kwargs):
        raise requests.exceptions.ConnectTimeout
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    with pytest.raises(RuntimeError):
        send_get_request(mock_url)