import pytest
from src.ip_validator import validate_ip_address

def test_valid_ip_addresses():
    """Test valid IP address formats"""
    valid_ips = [
        "1.2.3.4",
        "0.0.0.0",
        "9.9.9.9"
    ]
    for ip in valid_ips:
        assert validate_ip_address(ip) is True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test various invalid IP address formats"""
    invalid_ips = [
        "10.2.3.4",     # First octet > 9
        "1.20.3.4",     # Second octet > 9
        "1.2.30.4",     # Third octet > 9
        "1.2.3.40",     # Fourth octet > 9
        "1.2.3",        # Too few octets
        "1.2.3.4.5",    # Too many octets
        "a.b.c.d",      # Non-numeric characters
        "",             # Empty string
        "1.2.3.",       # Trailing dot
        ".1.2.3",       # Leading dot
        "1..2.3",       # Double dot
        "1.2.3.4 ",     # Trailing space
        " 1.2.3.4"      # Leading space
    ]
    for ip in invalid_ips:
        assert validate_ip_address(ip) is False, f"{ip} should be invalid"

def test_input_type():
    """Test input type validation"""
    assert validate_ip_address(123) is False
    assert validate_ip_address(None) is False
    assert validate_ip_address([]) is False