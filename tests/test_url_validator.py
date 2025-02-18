import pytest
from src.url_validator import is_valid_url

def test_valid_urls():
    """Test various valid URL formats"""
    valid_urls = [
        'https://www.example.com',
        'http://subdomain.example.co.uk',
        'https://example.com/path',
        'http://localhost',
        'ftp://files.example.com',
        'https://example.com:8080',
    ]
    for url in valid_urls:
        assert is_valid_url(url), f"{url} should be valid"

def test_invalid_urls():
    """Test various invalid URL formats"""
    invalid_urls = [
        '',  # Empty string
        'not a url',
        'www.example.com',  # Missing scheme
        'https://',  # Incomplete URL
        'http://.',  # Invalid domain
        123,  # Non-string input
        None,  # None input
    ]
    for url in invalid_urls:
        assert not is_valid_url(url), f"{url} should be invalid"

def test_edge_cases():
    """Test edge case URLs"""
    edge_case_urls = [
        'https://example.com/',  # URL with trailing slash
        'http://example.com?param=value',  # URL with query params
        'https://example.com#section',  # URL with fragment
    ]
    for url in edge_case_urls:
        assert is_valid_url(url), f"{url} should be valid"