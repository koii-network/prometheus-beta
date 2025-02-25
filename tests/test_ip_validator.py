import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    """Test various valid IP addresses."""
    valid_ips = [
        "0.0.0.0",
        "255.255.255.255", 
        "192.168.1.1", 
        "10.0.0.1", 
        "127.0.0.1"
    ]
    for ip in valid_ips:
        assert is_valid_ip_address(ip) == True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test various invalid IP addresses."""
    invalid_ips = [
        "256.0.0.1",       # Octet > 255
        "1.2.3.4.5",       # Too many octets
        "1.2.3",           # Too few octets
        "01.02.03.04",     # Leading zeros
        "1.2.3.04",        # Leading zero
        "1.2.3.-1",        # Negative number
        "1.2.3.a",         # Non-numeric 
        "",                # Empty string
        "   ",             # Whitespace
        None               # None type
    ]
    for ip in invalid_ips:
        assert is_valid_ip_address(ip) == False, f"{ip} should be invalid"

def test_edge_cases():
    """Test edge case IP addresses."""
    edge_cases = [
        "0.0.0.0",         # All zeros
        "255.255.255.255"  # All 255s
    ]
    for ip in edge_cases:
        assert is_valid_ip_address(ip) == True, f"{ip} should be valid"