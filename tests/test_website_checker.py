import pytest
import requests
from src.website_checker import is_website_online

def test_valid_website():
    """Test a known reliable website."""
    assert is_website_online('https://www.google.com') == True

def test_nonexistent_website():
    """Test a clearly non-existent website."""
    assert is_website_online('https://thisisnotarealwebsite123456.com') == False

def test_invalid_url_input():
    """Test handling of invalid URL inputs."""
    with pytest.raises(ValueError):
        is_website_online('')
    
    with pytest.raises(ValueError):
        is_website_online(None)

def test_url_without_scheme():
    """Test that URLs without a scheme are handled correctly."""
    assert is_website_online('google.com') == True

def test_extremely_short_timeout():
    """Test very short timeout."""
    assert is_website_online('google.com', timeout=0.01) in [True, False]

@pytest.mark.parametrize('url', [
    'http://example.com',
    'https://www.github.com',
    'www.openai.com'
])
def test_multiple_urls(url):
    """Test multiple different URLs."""
    assert isinstance(is_website_online(url), bool)