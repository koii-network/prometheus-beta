import pytest
from src.url_validator import is_valid_url

def test_valid_http_urls():
    assert is_valid_url('http://www.example.com') == True
    assert is_valid_url('https://example.com') == True
    assert is_valid_url('https://www.example.co.uk/path') == True
    assert is_valid_url('http://subdomain.example.com/page') == True

def test_valid_special_urls():
    assert is_valid_url('ftp://files.example.com') == True
    assert is_valid_url('mailto:user@example.com') == True
    assert is_valid_url('file:///path/to/file') == True

def test_invalid_urls():
    assert is_valid_url('') == False
    assert is_valid_url('   ') == False
    assert is_valid_url('not a url') == False
    assert is_valid_url('www.example.com') == False  # Missing scheme
    assert is_valid_url('example') == False

def test_edge_cases():
    assert is_valid_url(None) == False
    assert is_valid_url(123) == False
    assert is_valid_url([]) == False

def test_urls_with_special_characters():
    assert is_valid_url('https://example.com/path?param=value') == True
    assert is_valid_url('https://example.com/path#section') == True
    assert is_valid_url('https://example.com/path-with-hyphens') == True