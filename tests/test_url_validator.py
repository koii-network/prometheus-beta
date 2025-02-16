import pytest
from src.url_validator import is_valid_url

def test_valid_urls():
    # Test various valid URL formats
    valid_urls = [
        "http://www.example.com",
        "https://example.com",
        "https://sub.domain.com/path",
        "http://localhost",
        "https://example.com:8080",
        "ftp://files.example.com",
        "http://192.168.1.1",
        "https://example.com/path?param=value",
        "http://example.com/path#section"
    ]
    
    for url in valid_urls:
        assert is_valid_url(url), f"Failed to validate: {url}"

def test_invalid_urls():
    # Test various invalid URL formats
    invalid_urls = [
        "",  # Empty string
        "   ",  # Whitespace
        None,  # None type
        "not a url",  # No scheme
        "www.example.com",  # Missing scheme
        "http:/",  # Incomplete scheme
        "://example.com",  # Invalid scheme
        123,  # Non-string input
        "https://",  # Only scheme
        "http://."  # Invalid domain
    ]
    
    for url in invalid_urls:
        assert not is_valid_url(url), f"Incorrectly validated: {url}"

def test_edge_cases():
    # Additional edge case testing
    assert not is_valid_url(f"{'x' * 10000}")  # Extremely long string
    assert is_valid_url("http://example.com/with spaces")  # URLs with spaces
    assert is_valid_url("https://ümlaut.com")  # International domain