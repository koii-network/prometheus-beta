import pytest
import requests
from src.http_request import send_get_request

def test_send_get_request_success(mocker):
    """Test successful GET request"""
    mock_url = 'https://example.com/api'
    mock_response = {'key': 'value'}
    
    mock_response_obj = mocker.Mock()
    mock_response_obj.status_code = 200
    mock_response_obj.headers = {'Content-Type': 'application/json'}
    mock_response_obj.text = str(mock_response)
    mock_response_obj.json.return_value = mock_response
    mock_response_obj.raise_for_status = mocker.Mock()
    
    mocker.patch('requests.get', return_value=mock_response_obj)
    
    result = send_get_request(mock_url)
    
    assert result['status_code'] == 200
    assert result['json'] == mock_response

def test_send_get_request_with_headers(mocker):
    """Test GET request with custom headers"""
    mock_url = 'https://example.com/api'
    mock_headers = {'Authorization': 'Bearer token123'}
    
    mock_response_obj = mocker.Mock()
    mock_response_obj.status_code = 200
    mock_response_obj.json.return_value = {}
    mock_response_obj.headers = {}
    mock_response_obj.text = ''
    mock_response_obj.raise_for_status = mocker.Mock()
    
    mock_get = mocker.patch('requests.get', return_value=mock_response_obj)
    
    result = send_get_request(mock_url, headers=mock_headers)
    mock_get.assert_called_with(
        mock_url, 
        headers=mock_headers, 
        params={}, 
        timeout=10
    )
    assert result['status_code'] == 200

def test_send_get_request_with_params(mocker):
    """Test GET request with query parameters"""
    mock_url = 'https://example.com/api'
    mock_params = {'page': 1, 'limit': 10}
    
    mock_response_obj = mocker.Mock()
    mock_response_obj.status_code = 200
    mock_response_obj.json.return_value = {}
    mock_response_obj.headers = {}
    mock_response_obj.text = ''
    mock_response_obj.raise_for_status = mocker.Mock()
    
    mock_get = mocker.patch('requests.get', return_value=mock_response_obj)
    
    result = send_get_request(mock_url, params=mock_params)
    mock_get.assert_called_with(
        mock_url, 
        headers={}, 
        params=mock_params, 
        timeout=10
    )
    assert result['status_code'] == 200

def test_send_get_request_invalid_url():
    """Test handling of invalid URL"""
    with pytest.raises(ValueError):
        send_get_request("")
    
    with pytest.raises(ValueError):
        send_get_request(None)

def test_send_get_request_network_error(mocker):
    """Test network-related request errors"""
    mock_url = 'https://example.com/api'
    
    mocker.patch('requests.get', side_effect=requests.exceptions.ConnectTimeout)
    
    with pytest.raises(RuntimeError):
        send_get_request(mock_url)