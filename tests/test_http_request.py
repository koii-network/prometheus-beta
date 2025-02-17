import pytest
import requests
import json
from unittest.mock import patch
from src.http_request import send_get_request

class MockResponse:
    def __init__(self, status_code=200, headers=None, text='', json_data=None):
        self.status_code = status_code
        self.headers = headers or {}
        self.text = text
        self._json = json_data
        
    def json(self):
        return self._json
    
    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.HTTPError(f"HTTP Error {self.status_code}")

def test_send_get_request_success():
    # Test successful GET request
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(
            status_code=200, 
            headers={'content-type': 'application/json'},
            text='{"key": "value"}',
            json_data={'key': 'value'}
        )
        mock_get.return_value = mock_response
        
        result = send_get_request('https://example.com')
        
        assert result['status_code'] == 200
        assert result['json'] == {'key': 'value'}
        assert result['content'] == '{"key": "value"}'
        mock_get.assert_called_once_with('https://example.com', params=None, headers=None, timeout=10)

def test_send_get_request_with_params():
    # Test GET request with query parameters
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(status_code=200)
        mock_get.return_value = mock_response
        
        params = {'key1': 'value1', 'key2': 'value2'}
        result = send_get_request('https://example.com', params=params)
        
        mock_get.assert_called_once_with(
            'https://example.com', 
            params=params, 
            headers=None, 
            timeout=10
        )

def test_send_get_request_with_headers():
    # Test GET request with custom headers
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(status_code=200)
        mock_get.return_value = mock_response
        
        headers = {'Authorization': 'Bearer token'}
        result = send_get_request('https://example.com', headers=headers)
        
        mock_get.assert_called_once_with(
            'https://example.com', 
            params=None, 
            headers=headers, 
            timeout=10
        )

def test_send_get_request_timeout():
    # Test request timeout
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.Timeout('Connection timeout')
        
        with pytest.raises(requests.Timeout):
            send_get_request('https://example.com', timeout=5)

def test_send_get_request_http_error():
    # Test HTTP error response
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(status_code=404)
        mock_get.return_value = mock_response
        
        with pytest.raises(requests.HTTPError):
            send_get_request('https://example.com')

def test_send_get_request_connection_error():
    # Test connection error
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.ConnectionError('Connection failed')
        
        with pytest.raises(requests.ConnectionError):
            send_get_request('https://example.com')