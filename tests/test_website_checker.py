import pytest
import requests
from src.website_checker import is_website_online

class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

def test_valid_online_website(mocker):
    # Mock a successful request to a well-known website
    mocker.patch('requests.get', return_value=MockResponse(200))
    assert is_website_online('https://www.example.com') is True

def test_valid_redirected_website(mocker):
    # Mock a redirect response which is still considered online
    mocker.patch('requests.get', return_value=MockResponse(302))
    assert is_website_online('https://www.example.com') is True

def test_offline_website(mocker):
    # Mock a connection error
    mocker.patch('requests.get', side_effect=requests.ConnectionError())
    assert is_website_online('https://www.nonexistentwebsite12345.com') is False

def test_timeout_website(mocker):
    # Mock a timeout error
    mocker.patch('requests.get', side_effect=requests.Timeout())
    assert is_website_online('https://www.slowwebsite.com') is False

def test_invalid_url_none():
    with pytest.raises(ValueError, match="URL cannot be None"):
        is_website_online(None)

def test_invalid_url_empty_string():
    with pytest.raises(ValueError, match="URL cannot be empty"):
        is_website_online('   ')

def test_invalid_url_non_string():
    with pytest.raises(TypeError, match="URL must be a string"):
        is_website_online(123)

def test_malformed_url(mocker):
    # Mock a request exception for a malformed URL
    mocker.patch('requests.get', side_effect=requests.RequestException())
    assert is_website_online('not-a-valid-url') is False