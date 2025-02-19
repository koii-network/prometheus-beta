import pytest
from src.ip_validator import validate_ip_address

def test_valid_ip_addresses():
    # Test valid IP addresses
    valid_ips = [
        "1.2.3.4",
        "0.0.0.0",
        "9.9.9.9"
    ]
    for ip in valid_ips:
        assert validate_ip_address(ip) == True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    # Test invalid IP addresses
    invalid_ips = [
        "10.2.3.4",   # multi-digit parts
        "1.2.3.400",  # part out of range
        "1.2.3",      # too few parts
        "1.2.3.4.5",  # too many parts
        "a.b.c.d",    # non-numeric parts
        "",           # empty string
        "1.2.-3.4",   # negative number
        "1.2.3.",     # trailing dot
        " 1.2.3.4 ",  # extra whitespace
        None          # None input
    ]
    for ip in invalid_ips:
        assert validate_ip_address(ip) == False, f"{ip} should be invalid"