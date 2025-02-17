import pytest
import socket
from src.dns_lookup import perform_dns_lookup

def test_valid_hostname_lookup():
    """Test DNS lookup for a valid hostname."""
    result = perform_dns_lookup('google.com')
    # Validate that the result looks like an IP address
    assert isinstance(result, str)
    # Basic IP address format validation
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
        perform_dns_lookup('invalid.hostname.that.does.not.exist')

def test_ip_address_lookup():
    """Test DNS lookup works with both domain names and IP addresses."""
    # Some commonly used IP addresses
    test_cases = [
        'google.com',
        'www.python.org',
        '8.8.8.8',  # Google's public DNS
        '1.1.1.1',  # Cloudflare's DNS
    ]
    
    for hostname in test_cases:
        result = perform_dns_lookup(hostname)
        assert isinstance(result, str)
        # Validate IP address format
        parts = result.split('.')
        assert len(parts) == 4
        for part in parts:
            assert part.isdigit()
            assert 0 <= int(part) <= 255