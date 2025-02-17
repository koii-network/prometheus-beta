import pytest
import requests
from unittest.mock import patch
import json

# Import the function to test
from src.http_request import send_get_request

class MockResponse:
    def __init__(self, status_code, text, headers=None, json_data=None):
        self.status_code = status_code
        self.text = text
        self.headers = headers or {}
        self._json = json_data

    def json(self):
        return self._json

    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.HTTPError(f"HTTP Error: {self.status_code}")

def test_send_get_request_successful():
    # Mock a successful request
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(
            status_code=200, 
            text='{"key": "value"}', 
            headers={'Content-Type': 'application/json'},
            json_data={'key': 'value'}
        )
        mock_get.return_value = mock_response

        # Call the function
        result = send_get_request('https://example.com')

        # Assertions
        assert result['status_code'] == 200
        assert result['content'] == '{"key": "value"}'
        assert result['json'] == {'key': 'value'}
        assert 'Content-Type' in result['headers']

def test_send_get_request_with_headers():
    # Test with custom headers
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(
            status_code=200, 
            text='Success', 
            headers={'X-Custom-Header': 'test'}
        )
        mock_get.return_value = mock_response

        # Call the function
        headers = {'Authorization': 'Bearer token'}
        result = send_get_request('https://example.com', headers=headers)

        # Assertions
        assert result['status_code'] == 200
        mock_get.assert_called_once_with(
            'https://example.com', 
            headers=headers, 
            params=None, 
            timeout=10
        )

def test_send_get_request_with_params():
    # Test with query parameters
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(
            status_code=200, 
            text='Success', 
        )
        mock_get.return_value = mock_response

        # Call the function
        params = {'key1': 'value1', 'key2': 'value2'}
        result = send_get_request('https://example.com', params=params)

        # Assertions
        assert result['status_code'] == 200
        mock_get.assert_called_once_with(
            'https://example.com', 
            headers=None, 
            params=params, 
            timeout=10
        )

def test_send_get_request_invalid_url():
    # Test invalid URL
    with pytest.raises(ValueError):
        send_get_request('')

def test_send_get_request_network_error():
    # Test network error
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.RequestException("Network error")

        # Call the function and expect an exception
        with pytest.raises(requests.RequestException):
            send_get_request('https://example.com')

def test_send_get_request_non_json_response():
    # Test non-JSON response
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(
            status_code=200, 
            text='Plain text response'
        )
        mock_get.return_value = mock_response

        # Call the function
        result = send_get_request('https://example.com')

        # Assertions
        assert result['status_code'] == 200
        assert result['content'] == 'Plain text response'
        assert result['json'] is None