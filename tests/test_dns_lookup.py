import pytest
import socket
from src.dns_lookup import perform_dns_lookup

def test_successful_dns_lookup():
    """Test successful DNS lookup for a known hostname."""
    # Use a reliable hostname that should resolve
    result = perform_dns_lookup('google.com')
    
    # Check that the result looks like an IP address
    assert isinstance(result, str), "Result should be a string"
    
    # Validate IP address format (basic validation)
    parts = result.split('.')
    assert len(parts) == 4, "IP address should have 4 parts"
    for part in parts:
        assert part.isdigit(), "Each part should be a number"
        assert 0 <= int(part) <= 255, "Each part should be between 0 and 255"

def test_empty_hostname():
    """Test that an empty hostname raises a ValueError."""
    with pytest.raises(ValueError, match="Hostname cannot be empty"):
        perform_dns_lookup('')

def test_none_hostname():
    """Test that None hostname raises a ValueError."""
    with pytest.raises(ValueError, match="Hostname cannot be empty"):
        perform_dns_lookup(None)

def test_invalid_hostname():
    """Test that an invalid hostname raises a socket.gaierror."""
    with pytest.raises(socket.gaierror):
        perform_dns_lookup('invalid.nonexistent.domain')