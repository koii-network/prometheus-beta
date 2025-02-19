import pytest
from src.ip_validator import validate_ip_address

def test_valid_ip_addresses():
    """Test a variety of valid IP addresses"""
    valid_ips = [
        "1.2.3.4",
        "0.0.0.0", 
        "9.9.9.9",
        "5.6.7.8"
    ]
    for ip in valid_ips:
        assert validate_ip_address(ip) is True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test various invalid IP address formats"""
    invalid_ips = [
        # Multi-digit parts
        "10.2.3.4",
        "1.20.3.4", 
        "1.2.30.4",
        "1.2.3.40",
        
        # Non-numeric parts
        "a.2.3.4",
        "1.b.3.4",
        "1.2.c.4",
        "1.2.3.d",
        
        # Negative or out of range
        "-1.2.3.4",
        "1.2.3.10",
        
        # Wrong number of parts
        "1.2.3",
        "1.2.3.4.5",
        
        # Non-string input
        123,
        None,
        []
    ]
    for ip in invalid_ips:
        assert validate_ip_address(ip) is False, f"{ip} should be invalid"

def test_empty_string():
    """Test empty string"""
    assert validate_ip_address("") is False

def test_whitespace_input():
    """Test whitespace input"""
    assert validate_ip_address(" 1.2.3.4 ") is False