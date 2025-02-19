import pytest
from src.ip_validator import validate_ip_address

def test_valid_ip_addresses():
    # Test valid single-digit IP addresses
    assert validate_ip_address('1.2.3.4') == True
    assert validate_ip_address('0.0.0.0') == True
    assert validate_ip_address('9.9.9.9') == True

def test_invalid_ip_addresses():
    # Test addresses with multiple-digit octets
    assert validate_ip_address('10.2.3.4') == False
    assert validate_ip_address('1.22.3.4') == False
    
    # Test addresses with non-numeric characters
    assert validate_ip_address('a.2.3.4') == False
    assert validate_ip_address('1.b.3.4') == False
    
    # Test addresses with incorrect format
    assert validate_ip_address('1.2.3') == False
    assert validate_ip_address('1.2.3.4.5') == False
    assert validate_ip_address('1.2.3.') == False
    assert validate_ip_address('.1.2.3') == False

def test_edge_cases():
    # Test non-string inputs
    assert validate_ip_address(None) == False
    assert validate_ip_address(123) == False
    assert validate_ip_address([1,2,3,4]) == False

def test_boundary_condition():
    # Test boundary conditions for single-digit numbers
    assert validate_ip_address('0.0.0.0') == True
    assert validate_ip_address('9.9.9.9') == True