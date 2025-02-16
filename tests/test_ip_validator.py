import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    # Test standard valid IP addresses
    assert is_valid_ip_address('192.168.0.1') == True
    assert is_valid_ip_address('0.0.0.0') == True
    assert is_valid_ip_address('255.255.255.255') == True

def test_invalid_ip_addresses():
    # Test invalid IP addresses
    assert is_valid_ip_address('256.0.0.1') == False  # Octet > 255
    assert is_valid_ip_address('1.2.3.4.5') == False  # Too many octets
    assert is_valid_ip_address('1.2.3') == False  # Too few octets
    assert is_valid_ip_address('192.168.01.1') == False  # Leading zero
    assert is_valid_ip_address('192.168.1.01') == False  # Leading zero
    assert is_valid_ip_address('') == False  # Empty string
    assert is_valid_ip_address('not an ip') == False  # Non-numeric input

def test_edge_cases():
    # Test edge cases
    assert is_valid_ip_address('-1.0.0.0') == False  # Negative number
    assert is_valid_ip_address('192.168.-1.1') == False  # Negative number
    assert is_valid_ip_address(123) == False  # Non-string input
    assert is_valid_ip_address(None) == False  # None input