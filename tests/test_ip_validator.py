import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    # Test standard valid IP addresses
    assert is_valid_ip_address('192.168.0.1') == True
    assert is_valid_ip_address('0.0.0.0') == True
    assert is_valid_ip_address('255.255.255.255') == True

def test_invalid_ip_addresses():
    # Test various invalid IP address formats
    assert is_valid_ip_address('256.0.0.1') == False  # Out of range
    assert is_valid_ip_address('1.2.3.4.5') == False  # Too many octets
    assert is_valid_ip_address('1.2.3') == False  # Too few octets
    assert is_valid_ip_address('192.168.0') == False  # Incomplete IP
    assert is_valid_ip_address('192.168.0.a') == False  # Non-numeric
    assert is_valid_ip_address('01.02.03.04') == False  # Leading zeros

def test_edge_cases():
    # Test edge case inputs
    assert is_valid_ip_address('') == False
    assert is_valid_ip_address(None) == False
    assert is_valid_ip_address(123) == False  # Non-string input
    assert is_valid_ip_address('  192.168.0.1  ') == False  # Whitespace