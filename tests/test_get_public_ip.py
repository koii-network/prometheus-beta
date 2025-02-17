import pytest
import requests
from unittest.mock import patch
from src.get_public_ip import get_public_ip, _validate_ip_address

def test_get_public_ip_success():
    """Test successful retrieval of public IP."""
    with patch('requests.get') as mock_get:
        # Simulate a successful response
        mock_response = mock_get.return_value
        mock_response.text = '8.8.8.8'
        mock_response.raise_for_status.return_value = None
        
        ip = get_public_ip()
        assert _validate_ip_address(ip)

def test_get_public_ip_multiple_services():
    """Test IP retrieval falls back to alternate services."""
    with patch('requests.get') as mock_get:
        # First service fails, second succeeds
        mock_responses = [
            type('MockResponse1', (), {
                'raise_for_status': lambda: (_ for _ in ()).throw(requests.RequestException),
            }),
            type('MockResponse2', (), {
                'text': '1.2.3.4',
                'raise_for_status': lambda: None,
            })
        ]
        mock_get.side_effect = mock_responses
        
        ip = get_public_ip()
        assert ip == '1.2.3.4'

def test_get_public_ip_failure():
    """Test complete failure to retrieve IP."""
    with patch('requests.get') as mock_get:
        # All services fail
        mock_get.side_effect = requests.RequestException
        
        with pytest.raises(ConnectionError):
            get_public_ip()

def test_validate_ip_address():
    """Test IP address validation."""
    # Valid IP addresses
    assert _validate_ip_address('192.168.1.1') == True
    assert _validate_ip_address('0.0.0.0') == True
    assert _validate_ip_address('255.255.255.255') == True
    
    # Invalid IP addresses
    assert _validate_ip_address('256.0.0.1') == False
    assert _validate_ip_address('1.2.3.4.5') == False
    assert _validate_ip_address('abc.def.ghi.jkl') == False
    assert _validate_ip_address('') == False

def test_ip_address_format():
    """Ensure the IP retrieval returns a properly formatted IP."""
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.text = '8.8.8.8\n'  # With newline
        mock_response.raise_for_status.return_value = None
        
        ip = get_public_ip()
        assert ip == '8.8.8.8'  # Newline stripped