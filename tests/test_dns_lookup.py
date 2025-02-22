import pytest
import socket
from src.dns_lookup import perform_dns_lookup

def test_dns_lookup_valid_hostname():
    """Test DNS lookup with a well-known hostname."""
    result = perform_dns_lookup("google.com")
    assert result["hostname"] == "google.com"
    assert len(result["ipv4_addresses"]) > 0 or len(result["ipv6_addresses"]) > 0

def test_dns_lookup_localhost():
    """Test DNS lookup for localhost."""
    result = perform_dns_lookup("localhost")
    assert result["hostname"] == "localhost"
    assert "127.0.0.1" in result["ipv4_addresses"]

def test_dns_lookup_invalid_hostname():
    """Test DNS lookup with an invalid hostname."""
    with pytest.raises(socket.gaierror):
        perform_dns_lookup("invalid.nonexistent.domain")

def test_dns_lookup_empty_hostname():
    """Test DNS lookup with an empty hostname."""
    with pytest.raises(ValueError):
        perform_dns_lookup("")

def test_dns_lookup_none_hostname():
    """Test DNS lookup with None as hostname."""
    with pytest.raises(ValueError):
        perform_dns_lookup(None)

def test_dns_lookup_numeric_input():
    """Test DNS lookup with numeric input."""
    with pytest.raises(ValueError):
        perform_dns_lookup(123)

def test_dns_lookup_multiple_addresses():
    """Test DNS lookup that might return multiple addresses."""
    result = perform_dns_lookup("github.com")
    assert result["hostname"] == "github.com"
    assert isinstance(result["ipv4_addresses"], list)
    assert isinstance(result["ipv6_addresses"], list)