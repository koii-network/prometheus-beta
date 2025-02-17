import pytest
import requests
from src.public_ip import get_public_ip

class MockResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code
    
    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError("HTTP Error")

def test_get_public_ip_valid(monkeypatch):
    """Test getting a valid public IP address."""
    def mock_get(*args, **kwargs):
        return MockResponse('8.8.8.8')
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    ip = get_public_ip()
    assert ip == '8.8.8.8'

def test_get_public_ip_connection_error(monkeypatch):
    """Test handling of connection errors."""
    def mock_get(*args, **kwargs):
        raise requests.ConnectionError("Connection failed")
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    with pytest.raises(ConnectionError):
        get_public_ip()

def test_get_public_ip_invalid_format(monkeypatch):
    """Test handling of invalid IP address formats."""
    def mock_get(*args, **kwargs):
        return MockResponse('invalid.ip.address')
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    with pytest.raises(ValueError, match="Invalid IP address format"):
        get_public_ip()

def test_get_public_ip_out_of_range(monkeypatch):
    """Test handling of IP address with out-of-range octets."""
    def mock_get(*args, **kwargs):
        return MockResponse('256.0.0.1')
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    with pytest.raises(ValueError, match="Invalid IP address format"):
        get_public_ip()