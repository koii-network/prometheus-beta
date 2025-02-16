import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    # Test standard valid IP addresses
    assert is_valid_ip_address('192.168.1.1') == True
    assert is_valid_ip_address('0.0.0.0') == True
    assert is_valid_ip_address('255.255.255.255') == True

def test_invalid_ip_addresses():
    # Test invalid IP addresses
    assert is_valid_ip_address('256.1.2.3') == False  # Octet > 255
    assert is_valid_ip_address('1.2.3.4.5') == False  # Too many octets
    assert is_valid_ip_address('1.2.3') == False  # Too few octets
    assert is_valid_ip_address('01.2.3.4') == False  # Leading zero
    assert is_valid_ip_address('1.2.3.04') == False  # Leading zero

def test_non_numeric_inputs():
    # Test non-numeric and mixed inputs
    assert is_valid_ip_address('abc.def.ghi.jkl') == False
    assert is_valid_ip_address('1.2.3.a') == False
    assert is_valid_ip_address('1.2.3.-4') == False

def test_edge_cases():
    # Test various edge cases
    assert is_valid_ip_address('') == False
    assert is_valid_ip_address(None) == False
    assert is_valid_ip_address(123) == False  # Non-string input
    assert is_valid_ip_address('1.1.1.1 ') == False  # Extra whitespace
    assert is_valid_ip_address(' 1.1.1.1') == False  # Leading whitespace