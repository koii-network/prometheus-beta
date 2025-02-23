import pytest
import socket
from src.dns_lookup import perform_dns_lookup

def test_valid_hostname_lookup():
    """Test lookup of a valid hostname."""
    result = perform_dns_lookup('google.com')
    # Check result is a valid IP address
    assert isinstance(result, str)
    assert len(result.split('.')) == 4  # IPv4 address

def test_localhost_lookup():
    """Test lookup of localhost."""
    result = perform_dns_lookup('localhost')
    assert result == '127.0.0.1'

def test_invalid_hostname_raises_error():
    """Test that invalid hostname raises an error."""
    with pytest.raises(socket.gaierror):
        perform_dns_lookup('invalid.nonexistent.domain')

def test_empty_hostname_raises_error():
    """Test that empty hostname raises a ValueError."""
    with pytest.raises(ValueError):
        perform_dns_lookup('')

def test_none_hostname_raises_error():
    """Test that None hostname raises a ValueError."""
    with pytest.raises(ValueError):
        perform_dns_lookup(None)

def test_whitespace_hostname():
    """Test that whitespace-only hostname is handled."""
    with pytest.raises(ValueError):
        perform_dns_lookup('   ')

def test_numeric_hostname_raises_error():
    """Test that numeric input raises an error."""
    with pytest.raises(ValueError):
        perform_dns_lookup(123)