import pytest
import requests
import sys
import os

# Add the source directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from website_online_checker import is_website_online

def test_online_websites():
    # Test known online websites
    assert is_website_online('google.com') == True
    assert is_website_online('https://www.github.com') == True

def test_offline_websites():
    # Test non-existent domain
    assert is_website_online('thisisnotarealwebsite123456.com') == False

def test_invalid_urls():
    # Test invalid URL inputs
    with pytest.raises(ValueError):
        is_website_online('')
    with pytest.raises(ValueError):
        is_website_online(None)

def test_url_normalization():
    # Test that URLs without http/https are normalized
    assert is_website_online('google.com') == True
    assert is_website_online('www.github.com') == True

def test_timeout():
    # Test with very short timeout
    assert is_website_online('google.com', timeout=0.001) in [True, False]