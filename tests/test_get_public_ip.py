import pytest
import requests
from src.get_public_ip import get_public_ip

def test_get_public_ip_success(mocker):
    """Test successful retrieval of public IP address."""
    # Mock the requests.get method to return a predictable IP
    mock_response = mocker.Mock()
    mock_response.text = '123.45.67.89'
    mock_response.raise_for_status = mocker.Mock()
    mocker.patch('requests.get', return_value=mock_response)
    
    ip = get_public_ip()
    assert ip == '123.45.67.89'

def test_get_public_ip_connection_error(mocker):
    """Test handling of connection errors."""
    # Simulate a connection error
    mocker.patch('requests.get', side_effect=requests.RequestException('Connection failed'))
    
    with pytest.raises(ConnectionError):
        get_public_ip()

def test_get_public_ip_empty_response(mocker):
    """Test handling of empty IP response."""
    # Mock a response with empty text
    mock_response = mocker.Mock()
    mock_response.text = ''
    mock_response.raise_for_status = mocker.Mock()
    mocker.patch('requests.get', return_value=mock_response)
    
    with pytest.raises(ValueError, match="No IP address retrieved"):
        get_public_ip()

# Validate IP format (optional, but recommended)
def test_ip_address_format():
    """Validate that the IP address follows expected format."""
    import re
    
    # Retrieve the actual IP
    ip = get_public_ip()
    
    # IPv4 regex pattern
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    assert re.match(ip_pattern, ip), f"Invalid IP address format: {ip}"