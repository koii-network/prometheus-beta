import pytest
from src.url_validator import is_valid_url

def test_valid_urls():
    """Test a variety of valid URL formats"""
    valid_urls = [
        "http://www.example.com",
        "https://example.com",
        "https://www.example.co.uk",
        "ftp://files.example.com",
        "https://example.com/path",
        "https://example.com/path?param=value",
        "http://localhost",
        "https://127.0.0.1"
    ]
    for url in valid_urls:
        assert is_valid_url(url), f"{url} should be valid"

def test_invalid_urls():
    """Test various invalid URL formats"""
    invalid_urls = [
        "",  # Empty string
        None,  # None value
        "not a url",
        "www.example.com",  # Missing scheme
        "http://",  # Only scheme
        "https:///",  # No domain
        "invalid://example.com",  # Invalid scheme
        123  # Non-string input
    ]
    for url in invalid_urls:
        assert not is_valid_url(url), f"{url} should be invalid"

def test_edge_cases():
    """Test edge case URLs"""
    edge_case_urls = [
        "https://example-domain.com",  # Domain with hyphen
        "ftp://user:pass@example.com",  # URL with credentials
    ]
    for url in edge_case_urls:
        assert is_valid_url(url), f"{url} should be valid"