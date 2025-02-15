import pytest
import requests
from src.public_ip import get_public_ip

def test_get_public_ip_valid():
    """Test that get_public_ip returns a valid IP address."""
    ip = get_public_ip()
    
    # Validate IP address format using basic regex
    assert isinstance(ip, str), "IP should be a string"
    assert ip, "IP should not be empty"
    
    # Basic IP address validation
    ip_parts = ip.split('.')
    assert len(ip_parts) == 4, "IP should have 4 octets"
    
    for part in ip_parts:
        assert part.isdigit(), "IP octets should be numeric"
        assert 0 <= int(part) <= 255, "IP octets should be between 0 and 255"

def test_get_public_ip_network_error(mocker):
    """Test error handling when network request fails."""
    # Mock requests.get to raise a connection error
    mocker.patch('requests.get', side_effect=requests.ConnectionError("Network Error"))
    
    with pytest.raises(RuntimeError, match="Could not retrieve public IP address"):
        get_public_ip()