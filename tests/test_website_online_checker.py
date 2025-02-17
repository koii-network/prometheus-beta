import pytest
import requests
from src.website_online_checker import is_website_online

def test_is_website_online_valid_website():
    """Test a known reliable website that should be online."""
    assert is_website_online("https://www.google.com") == True

def test_is_website_online_invalid_website():
    """Test an invalid/non-existent website."""
    assert is_website_online("https://www.thiswillnotexist123456789.com") == False

def test_is_website_online_malformed_url():
    """Test a malformed URL."""
    assert is_website_online("not a valid url") == False

def test_is_website_online_timeout():
    """Test a timeout scenario."""
    # Use a fake IP that should timeout
    assert is_website_online("http://10.255.255.1", timeout=1) == False

def test_is_website_online_http_error_code():
    """Test a website that returns an error status code."""
    # Create a mock response with a 404 status code
    class MockResponse:
        status_code = 404

    # Temporarily patch the requests.get method
    def mock_get(*args, **kwargs):
        return MockResponse()

    original_get = requests.get
    requests.get = mock_get

    try:
        assert is_website_online("https://example.com") == False
    finally:
        # Restore the original requests.get method
        requests.get = original_get