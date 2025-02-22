import pytest
import requests
import re
from src.get_public_ip import get_public_ip

def test_get_public_ip_returns_valid_ip():
    """Test that the function returns a valid IP address."""
    ip_address = get_public_ip()
    
    # Check that the IP is a valid IPv4 address
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    assert ip_pattern.match(ip_address), f"Invalid IP address format: {ip_address}"

def test_get_public_ip_handles_network_errors(mocker):
    """Test error handling when network request fails."""
    # Mock requests.get to raise a RequestException
    mocker.patch('requests.get', side_effect=requests.RequestException("Network error"))
    
    with pytest.raises(ValueError, match="Could not retrieve public IP"):
        get_public_ip()

def test_get_public_ip_timeout(mocker):
    """Test timeout scenario."""
    # Mock requests.get to raise a Timeout exception
    mocker.patch('requests.get', side_effect=requests.Timeout("Request timed out"))
    
    with pytest.raises(ValueError, match="Could not retrieve public IP"):
        get_public_ip()