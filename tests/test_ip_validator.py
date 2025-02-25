import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    # Test standard valid IP addresses
    valid_ips = [
        "192.168.0.1",
        "255.255.255.255",
        "0.0.0.0",
        "10.20.30.40"
    ]
    for ip in valid_ips:
        assert is_valid_ip_address(ip) == True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    # Test invalid IP addresses
    invalid_ips = [
        "256.1.2.3",          # Out of range octet
        "1.2.3.4.5",          # Too many octets
        "1.2.3",              # Too few octets
        "01.02.03.04",        # Leading zeros
        "1.2.3.04",           # Leading zero in last octet
        "abc.def.ghi.jkl",    # Non-numeric
        "192.168.0",          # Incomplete
        "-1.0.0.0",           # Negative number
        "192.168.0.1.",       # Extra dot
        "...",                # Just dots
        "a.b.c.d",            # Alphabetic characters
        ""                    # Empty string
    ]
    for ip in invalid_ips:
        assert is_valid_ip_address(ip) == False, f"{ip} should be invalid"

def test_edge_cases():
    # Test edge case IP addresses
    assert is_valid_ip_address("0.0.0.0") == True
    assert is_valid_ip_address("255.255.255.255") == True