import pytest
import requests
from src.http_get_request import send_http_get_request

def test_successful_get_request(mocker):
    # Mock a successful request
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = '{"key": "value"}'
    mock_response.json.return_value = {"key": "value"}
    mock_response.headers = {'content-type': 'application/json'}
    
    mocker.patch('requests.get', return_value=mock_response)
    
    result = send_http_get_request('https://example.com')
    assert result['status_code'] == 200
    assert result['json'] == {"key": "value"}

def test_invalid_url():
    with pytest.raises(ValueError, match="Invalid or empty URL"):
        send_http_get_request('')
    
    with pytest.raises(ValueError, match="Invalid or empty URL"):
        send_http_get_request('invalid_url')

def test_request_exception(mocker):
    # Simulate a network error
    mocker.patch('requests.get', side_effect=requests.RequestException("Network error"))
    
    with pytest.raises(RuntimeError, match="HTTP GET request failed"):
        send_http_get_request('https://example.com')

def test_request_with_headers_and_params(mocker):
    # Mock a successful request with headers and params
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = 'Success'
    mock_response.headers = {'content-type': 'text/plain'}
    
    mock_get = mocker.patch('requests.get', return_value=mock_response)
    
    headers = {'Authorization': 'Bearer token'}
    params = {'key1': 'value1', 'key2': 'value2'}
    
    result = send_http_get_request('https://example.com', headers=headers, params=params)
    
    assert result['status_code'] == 200
    mock_get.assert_called_once_with(
        'https://example.com', 
        headers=headers, 
        params=params, 
        timeout=10
    )

def test_non_json_response(mocker):
    # Mock a non-JSON response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = 'Plain text response'
    mock_response.headers = {'content-type': 'text/plain'}
    
    mocker.patch('requests.get', return_value=mock_response)
    
    result = send_http_get_request('https://example.com')
    assert result['status_code'] == 200
    assert result['text'] == 'Plain text response'
    assert result['json'] is None