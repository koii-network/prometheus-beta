import pytest
import requests
from src.get_public_ip import get_public_ip

def test_get_public_ip(mocker):
    """
    Test successful retrieval of public IP address.
    """
    # Mock the requests.get method to return a predictable IP
    mock_response = mocker.Mock()
    mock_response.text = '8.8.8.8'
    mock_response.raise_for_status = mocker.Mock()
    mocker.patch('requests.get', return_value=mock_response)
    
    ip = get_public_ip()
    assert ip == '8.8.8.8'

def test_get_public_ip_connection_error(mocker):
    """
    Test handling of connection errors.
    """
    # Simulate a connection error
    mocker.patch('requests.get', side_effect=requests.ConnectionError("Network error"))
    
    with pytest.raises(ConnectionError):
        get_public_ip()

def test_get_public_ip_empty_response(mocker):
    """
    Test handling of empty IP response.
    """
    # Mock a response with empty text
    mock_response = mocker.Mock()
    mock_response.text = ''
    mock_response.raise_for_status = mocker.Mock()
    mocker.patch('requests.get', return_value=mock_response)
    
    with pytest.raises(ValueError):
        get_public_ip()