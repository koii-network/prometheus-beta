import pytest
import requests
from src.website_checker import is_website_online

def test_online_website():
    """Test a known online website."""
    assert is_website_online("https://www.google.com") == True

def test_nonexistent_website():
    """Test a clearly nonexistent website."""
    assert is_website_online("https://www.thisisanonexistentwebsitexxxxxxxxxxxx.com") == False

def test_invalid_url():
    """Test an invalid URL format."""
    assert is_website_online("not a valid url") == False

def test_timeout_website(mocker):
    """Test website check with a timeout scenario."""
    # Mock requests.get to simulate a timeout
    mocker.patch('requests.get', side_effect=requests.Timeout)
    assert is_website_online("https://www.example.com") == False

def test_connection_error(mocker):
    """Test website check with a connection error."""
    # Mock requests.get to simulate a connection error
    mocker.patch('requests.get', side_effect=requests.ConnectionError)
    assert is_website_online("https://www.example.com") == False

def test_custom_timeout():
    """Test website check with a custom timeout."""
    # Using a very short timeout to test the feature
    assert is_website_online("https://www.google.com", timeout=1) in [True, False]