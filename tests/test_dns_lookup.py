import pytest
import socket
from src.dns_lookup import perform_dns_lookup

def test_valid_hostname_lookup():
    """Test lookup of a known, resolvable hostname."""
    result = perform_dns_lookup('google.com')
    assert isinstance(result, str)
    # Validate IP address format
    import ipaddress
    ipaddress.ip_address(result)

def test_localhost_lookup():
    """Test lookup of localhost."""
    result = perform_dns_lookup('localhost')
    assert result in ['127.0.0.1', '::1']

def test_invalid_hostname_type():
    """Test error handling for non-string input."""
    with pytest.raises(ValueError, match="Hostname must be a string"):
        perform_dns_lookup(123)

def test_empty_hostname():
    """Test error handling for empty hostname."""
    with pytest.raises(ValueError, match="Hostname cannot be empty"):
        perform_dns_lookup('')
    with pytest.raises(ValueError, match="Hostname cannot be empty"):
        perform_dns_lookup('   ')

def test_unresolvable_hostname():
    """Test error handling for unresolvable hostname."""
    with pytest.raises(socket.gaierror):
        perform_dns_lookup('thishostnameshouldnotexist.invalid')

def test_whitespace_handling():
    """Test that whitespace is stripped from hostname."""
    result = perform_dns_lookup('  google.com  ')
    assert isinstance(result, str)
    # Validate IP address format
    import ipaddress
    ipaddress.ip_address(result)