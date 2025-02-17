import pytest
import requests
from unittest.mock import patch
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.public_ip import get_public_ip

def test_get_public_ip_success():
    """Test successful retrieval of public IP address."""
    with patch('requests.get') as mock_get:
        # Mock a successful response
        mock_response = mock_get.return_value
        mock_response.text = '123.456.789.101'
        mock_response.raise_for_status = lambda: None
        
        ip = get_public_ip()
        assert ip == '123.456.789.101'
        mock_get.assert_called_once_with('https://api.ipify.org', timeout=10)

def test_get_public_ip_connection_error():
    """Test handling of connection errors."""
    with patch('requests.get') as mock_get:
        # Simulate a connection error
        mock_get.side_effect = requests.ConnectionError("Network error")
        
        with pytest.raises(ConnectionError, match="Unable to retrieve public IP address"):
            get_public_ip()

def test_get_public_ip_timeout():
    """Test handling of request timeout."""
    with patch('requests.get') as mock_get:
        # Simulate a timeout error
        mock_get.side_effect = requests.Timeout("Request timed out")
        
        with pytest.raises(ConnectionError, match="Unable to retrieve public IP address"):
            get_public_ip()

def test_get_public_ip_http_error():
    """Test handling of HTTP errors."""
    with patch('requests.get') as mock_get:
        # Mock a response with HTTP error
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = requests.HTTPError("HTTP Error")
        
        with pytest.raises(ConnectionError, match="Unable to retrieve public IP address"):
            get_public_ip()