import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    # Test various valid IP addresses
    assert is_valid_ip_address('1.2.3.4') == True
    assert is_valid_ip_address('0.0.0.0') == True
    assert is_valid_ip_address('9.9.9.9') == True

def test_invalid_ip_addresses():
    # Test various invalid IP addresses
    assert is_valid_ip_address('10.2.3.4') == False  # Two-digit number
    assert is_valid_ip_address('1.2.3') == False  # Too few parts
    assert is_valid_ip_address('1.2.3.4.5') == False  # Too many parts
    assert is_valid_ip_address('a.b.c.d') == False  # Non-numeric characters
    assert is_valid_ip_address('1.2.3.') == False  # Incomplete address
    assert is_valid_ip_address('.1.2.3') == False  # Starts with a dot
    
def test_non_string_input():
    # Test non-string inputs
    assert is_valid_ip_address(12345) == False
    assert is_valid_ip_address(None) == False
    assert is_valid_ip_address([]) == False