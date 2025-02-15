import pytest
import socket

from src.dns_lookup import perform_dns_lookup

def test_successful_dns_lookup():
    # Test a well-known domain that should resolve
    result = perform_dns_lookup('google.com')
    # Validate that the result looks like an IP address
    assert isinstance(result, str)
    # Basic IP address format validation
    parts = result.split('.')
    assert len(parts) == 4
    for part in parts:
        assert part.isdigit()
        assert 0 <= int(part) <= 255

def test_dns_lookup_empty_hostname():
    # Test that an empty hostname raises a ValueError
    with pytest.raises(ValueError, match="Hostname cannot be empty"):
        perform_dns_lookup('')

def test_dns_lookup_none_hostname():
    # Test that None hostname raises a ValueError
    with pytest.raises(ValueError, match="Hostname cannot be empty"):
        perform_dns_lookup(None)

def test_invalid_hostname():
    # Test that an invalid hostname raises a socket.gaierror
    with pytest.raises(socket.gaierror):
        perform_dns_lookup('nonexistent.invalid.domain')