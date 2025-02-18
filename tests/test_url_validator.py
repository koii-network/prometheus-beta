import pytest
from src.url_validator import is_valid_url

def test_valid_urls():
    """Test various valid URL formats"""
    valid_urls = [
        'http://www.example.com',
        'https://example.com',
        'http://subdomain.example.com/path',
        'https://example.com:8080',
        'http://example.com/path?param=value',
        'https://example.com/path#section',
        'ftp://files.example.com'
    ]
    
    for url in valid_urls:
        assert is_valid_url(url), f"Failed to validate valid URL: {url}"

def test_invalid_urls():
    """Test various invalid URL formats"""
    invalid_urls = [
        '',  # Empty string
        '   ',  # Whitespace
        'not a url',
        'www.example.com',  # Missing scheme
        'http://',  # Missing netloc
        'https:///path',  # Missing netloc
        123,  # Non-string input
        None  # None input
    ]
    
    for url in invalid_urls:
        assert not is_valid_url(url), f"Incorrectly validated invalid URL: {url}"

def test_edge_cases():
    """Test edge case scenarios"""
    # URLs with special characters
    assert is_valid_url('http://example.com/path-with-hyphens')
    assert is_valid_url('https://example.com/path_with_underscores')
    
    # Extremely long URLs
    long_url = 'http://' + 'a' * 2000 + '.com'
    assert is_valid_url(long_url)
    
    # IDN (Internationalized Domain Names)
    assert is_valid_url('http://xn--80aswg.xn--p1ai')  # Punycode for a Russian domain