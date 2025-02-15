import pytest
import requests
from src.website_checker import is_website_online

def test_valid_online_websites():
    # Test some known reliable websites
    assert is_website_online('https://www.google.com') == True
    assert is_website_online('google.com') == True  # Test URL without protocol
    assert is_website_online('https://www.github.com') == True

def test_invalid_or_nonexistent_websites():
    # Test non-existent or deliberately incorrect websites
    assert is_website_online('https://www.nonexistentwebsite123456.com') == False
    assert is_website_online('invalid-url') == False

def test_invalid_input():
    # Test invalid input types
    with pytest.raises(ValueError):
        is_website_online('')
    with pytest.raises(ValueError):
        is_website_online(None)

def test_custom_timeout():
    # Test custom timeout 
    assert is_website_online('https://www.google.com', timeout=2) == True

def test_http_and_https_urls():
    # Test both HTTP and HTTPS protocols
    assert is_website_online('http://www.example.com') == True
    assert is_website_online('https://www.example.com') == True