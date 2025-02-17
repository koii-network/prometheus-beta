import pytest
import requests
from src.website_checker import is_website_online

def test_online_website():
    """Test a known online website"""
    assert is_website_online('https://www.google.com') == True

def test_online_website_without_protocol():
    """Test a known online website without explicit protocol"""
    assert is_website_online('www.google.com') == True

def test_non_existent_website():
    """Test a non-existent website"""
    assert is_website_online('https://this-website-does-not-exist-12345.com') == False

def test_invalid_input_empty_string():
    """Test empty string input"""
    with pytest.raises(ValueError):
        is_website_online('')

def test_invalid_input_none():
    """Test None input"""
    with pytest.raises(ValueError):
        is_website_online(None)

def test_invalid_input_number():
    """Test non-string input"""
    with pytest.raises(ValueError):
        is_website_online(12345)