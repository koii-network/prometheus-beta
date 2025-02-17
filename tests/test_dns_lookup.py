import pytest
import socket
from src.dns_lookup import perform_dns_lookup

def test_valid_hostname_lookup():
    """Test lookup of a known valid hostname."""
    result = perform_dns_lookup('google.com')
    # Check if result is a valid IP address format
    assert isinstance(result, str)
    # Validate IP address pattern (basic check)
    parts = result.split('.')
    assert len(parts) == 4
    for part in parts:
        assert part.isdigit()
        assert 0 <= int(part) <= 255

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
        perform_dns_lookup('this.is.not.a.real.hostname.xyz')

def test_localhost_lookup():
    """Test lookup of localhost."""
    result = perform_dns_lookup('localhost')
    assert result in ['127.0.0.1', '::1']