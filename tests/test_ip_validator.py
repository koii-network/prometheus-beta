import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    """Test various valid IP addresses."""
    valid_ips = [
        '0.0.0.0',
        '255.255.255.255',
        '192.168.0.1',
        '10.0.0.1',
        '172.16.0.1'
    ]
    
    for ip in valid_ips:
        assert is_valid_ip_address(ip) is True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test various invalid IP addresses."""
    invalid_ips = [
        # Out of range
        '256.0.0.0',
        '0.256.0.0',
        '0.0.256.0',
        '0.0.0.256',
        
        # Leading zeros
        '01.0.0.0',
        '0.01.0.0',
        '0.0.01.0',
        '0.0.0.01',
        
        # Non-numeric
        'a.b.c.d',
        '192.168.0.x',
        
        # Incorrect format
        '192.168.0',  # Too few octets
        '192.168.0.1.2',  # Too many octets
        '192.168.0.',  # Empty last octet
        '.192.168.0.1',  # Empty first octet
        
        # Non-string inputs
        123,
        None,
        []
    ]
    
    for ip in invalid_ips:
        assert is_valid_ip_address(ip) is False, f"{ip} should be invalid"

def test_edge_cases():
    """Test edge case IP addresses."""
    edge_cases = [
        '0.0.0.0',  # Minimum possible
        '255.255.255.255'  # Maximum possible
    ]
    
    for ip in edge_cases:
        assert is_valid_ip_address(ip) is True, f"{ip} should be valid"