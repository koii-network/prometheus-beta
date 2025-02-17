import pytest
import requests
from src.website_checker import is_website_online

def test_is_website_online_valid_websites():
    # Test some well-known websites that are typically online
    assert is_website_online('www.google.com') == True
    assert is_website_online('google.com') == True
    assert is_website_online('https://www.github.com') == True

def test_is_website_online_invalid_websites():
    # Test some clearly non-existent websites
    assert is_website_online('www.nonexistentwebsite123456.com') == False
    assert is_website_online('invalid.domain') == False

def test_is_website_online_edge_cases():
    # Test empty string
    assert is_website_online('') == False
    
    # Test None input
    with pytest.raises(TypeError):
        is_website_online(None)

def test_is_website_online_timeout(mocker):
    # Simulate a timeout scenario
    mocker.patch('requests.get', side_effect=requests.Timeout)
    assert is_website_online('www.example.com') == False

def test_is_website_online_connection_error(mocker):
    # Simulate a connection error scenario
    mocker.patch('requests.get', side_effect=requests.ConnectionError)
    assert is_website_online('www.example.com') == False