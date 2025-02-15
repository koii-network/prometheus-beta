import pytest
import requests
from unittest.mock import patch
from src.http_request import send_get_request

class MockResponse:
    def __init__(self, status_code=200, text='', json_data=None, headers=None):
        self.status_code = status_code
        self.text = text
        self._json = json_data
        self.headers = headers or {}

    def json(self):
        if self._json is None:
            raise ValueError("No JSON")
        return self._json

    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.HTTPError(f"HTTP Error {self.status_code}")

def test_send_get_request_success():
    with patch('requests.get') as mock_get:
        # Simulate a successful JSON response
        mock_response = MockResponse(
            status_code=200, 
            text='{"key": "value"}', 
            json_data={'key': 'value'},
            headers={'Content-Type': 'application/json'}
        )
        mock_get.return_value = mock_response

        result = send_get_request('http://example.com')
        
        # Verify the result structure
        assert result['status_code'] == 200
        assert result['content'] == '{"key": "value"}'
        assert result['json'] == {'key': 'value'}
        assert 'Content-Type' in result['headers']

def test_send_get_request_with_params():
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(status_code=200, text='success')
        mock_get.return_value = mock_response

        result = send_get_request(
            'http://example.com', 
            params={'param1': 'value1'},
            headers={'Authorization': 'Bearer token'}
        )
        
        # Verify the request was made with correct params and headers
        mock_get.assert_called_once_with(
            'http://example.com', 
            params={'param1': 'value1'},
            headers={'Authorization': 'Bearer token'},
            timeout=10
        )

def test_send_get_request_network_error():
    with patch('requests.get') as mock_get:
        # Simulate a network error
        mock_get.side_effect = requests.ConnectionError("Network error")

        with pytest.raises(requests.ConnectionError):
            send_get_request('http://example.com')

def test_send_get_request_http_error():
    with patch('requests.get') as mock_get:
        # Simulate an HTTP error response
        mock_response = MockResponse(status_code=404, text='Not Found')
        mock_response.raise_for_status = lambda: exec('raise requests.HTTPError("404 Not Found")')
        mock_get.return_value = mock_response

        with pytest.raises(requests.HTTPError):
            send_get_request('http://example.com')

def test_send_get_request_no_json():
    with patch('requests.get') as mock_get:
        # Simulate a response without JSON
        mock_response = MockResponse(status_code=200, text='Plain text response')
        mock_get.return_value = mock_response

        result = send_get_request('http://example.com')
        
        assert result['status_code'] == 200
        assert result['content'] == 'Plain text response'
        assert result['json'] is None