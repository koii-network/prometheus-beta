import pytest
import requests
from src.website_checker import is_website_online

def test_valid_online_website():
    """Test a known online website."""
    assert is_website_online('https://www.google.com') == True

def test_invalid_website():
    """Test a non-existent website."""
    assert is_website_online('https://www.nonexistentwebsitetest123456.com') == False

def test_malformed_url():
    """Test handling of malformed URLs."""
    assert is_website_online('invalid url') == False

def test_empty_url():
    """Test handling of empty URL."""
    with pytest.raises(ValueError):
        is_website_online('')

def test_none_url():
    """Test handling of None input."""
    with pytest.raises(TypeError):
        is_website_online(None)

def test_url_without_protocol():
    """Test URL without protocol."""
    assert is_website_online('google.com') == True

def test_short_timeout():
    """Test with very short timeout."""
    assert is_website_online('https://www.google.com', timeout=0.001) in [True, False]

# Mocking tests to simulate different scenarios
def test_connection_error(mocker):
    """Test handling of connection errors."""
    # Mock requests.head to raise a ConnectionError
    mocker.patch('requests.head', side_effect=requests.ConnectionError)
    assert is_website_online('https://www.example.com') == False

def test_timeout_error(mocker):
    """Test handling of timeout errors."""
    # Mock requests.head to raise a Timeout error
    mocker.patch('requests.head', side_effect=requests.Timeout)
    assert is_website_online('https://www.example.com') == False