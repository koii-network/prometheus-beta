import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    """Test various valid IP addresses."""
    valid_ips = [
        '0.0.0.0',
        '192.168.0.1',
        '255.255.255.255',
        '1.2.3.4'
    ]
    for ip in valid_ips:
        assert is_valid_ip_address(ip), f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test various invalid IP addresses."""
    invalid_ips = [
        '256.0.0.1',  # Octet out of range
        '1.2.3.4.5',  # Too many octets
        '1.2.3',      # Too few octets
        '01.02.03.04',  # Leading zeros
        '1.2.3.04',   # Leading zero
        '192.168.0.1.',  # Extra dot
        '.192.168.0.1',  # Leading dot
        'abc.def.ghi.jkl',  # Non-numeric
        '',           # Empty string
        '   ',        # Whitespace
        '192.168.0',  # Incomplete IP
        '192.168.0.1.2'  # Too many segments
    ]
    for ip in invalid_ips:
        assert not is_valid_ip_address(ip), f"{ip} should be invalid"

def test_non_string_input():
    """Test non-string inputs."""
    non_string_inputs = [
        123,
        None,
        ['192.168.0.1'],
        {'ip': '192.168.0.1'}
    ]
    for input_val in non_string_inputs:
        assert not is_valid_ip_address(input_val), f"{input_val} should be invalid"

def test_edge_cases():
    """Test edge case IP addresses."""
    edge_cases = [
        '0.0.0.0',    # All zeros
        '255.255.255.255'  # All 255s
    ]
    for ip in edge_cases:
        assert is_valid_ip_address(ip), f"{ip} should be valid"