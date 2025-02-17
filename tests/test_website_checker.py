import pytest
from src.website_checker import is_website_online

def test_online_website():
    """Test that a known online website returns True"""
    assert is_website_online('google.com') == True
    assert is_website_online('https://www.python.org') == True

def test_offline_website():
    """Test that an invalid website returns False"""
    assert is_website_online('nonexistentwebsite123456.com') == False
    assert is_website_online('https://www.thissitedoesnotexist987654.com') == False

def test_url_variations():
    """Test different URL formats"""
    assert is_website_online('google.com') == True
    assert is_website_online('www.google.com') == True
    assert is_website_online('https://google.com') == True

def test_url_with_timeout():
    """Test website check with custom timeout"""
    assert is_website_online('google.com', timeout=2) == True
    assert is_website_online('google.com', timeout=1) == True