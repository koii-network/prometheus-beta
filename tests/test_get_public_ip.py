import pytest
import requests
from unittest.mock import patch
from src.get_public_ip import get_public_ip

def test_get_public_ip_success():
    # Test successful IP retrieval
    with patch('requests.get') as mock_get:
        mock_get.return_value.text = '8.8.8.8'
        mock_get.return_value.raise_for_status.return_value = None
        
        ip = get_public_ip()
        assert ip == '8.8.8.8'

def test_get_public_ip_multiple_services():
    # Test multiple service fallback
    with patch('requests.get') as mock_get:
        # First service fails
        mock_get.side_effect = [
            requests.exceptions.RequestException(),
            type('Response', (), {'text': '1.2.3.4', 'raise_for_status': lambda: None})()
        ]
        
        ip = get_public_ip()
        assert ip == '1.2.3.4'

def test_get_public_ip_invalid_ip():
    # Test invalid IP format
    with patch('requests.get') as mock_get:
        mock_get.return_value.text = 'not an ip'
        mock_get.return_value.raise_for_status.return_value = None
        
        with pytest.raises(ConnectionError):
            get_public_ip()

def test_get_public_ip_all_services_fail():
    # Test when all services fail
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException()
        
        with pytest.raises(ConnectionError):
            get_public_ip()