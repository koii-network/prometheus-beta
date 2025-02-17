import pytest
import requests
import sys
import os

# Add the source directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from website_online_checker import is_website_online
from unittest.mock import patch

def test_valid_mock_connection():
    # Mock a successful connection
    with patch('requests.head') as mock_head:
        mock_response = mock_head.return_value
        mock_response.status_code = 200
        assert is_website_online('example.com') == True

def test_failed_mock_connection():
    # Mock a failed connection
    with patch('requests.head') as mock_head:
        mock_head.side_effect = requests.ConnectionError()
        assert is_website_online('example.com') == False

def test_invalid_urls():
    # Test invalid URL inputs
    with pytest.raises(ValueError):
        is_website_online('')
    with pytest.raises(ValueError):
        is_website_online(None)

def test_url_normalization():
    # Test that URLs without http/https are normalized
    with patch('requests.head') as mock_head:
        mock_response = mock_head.return_value
        mock_response.status_code = 200
        assert is_website_online('google.com') == True

def test_timeout():
    # Mock a timeout scenario
    with patch('requests.head') as mock_head:
        mock_head.side_effect = requests.Timeout()
        assert is_website_online('example.com') == False