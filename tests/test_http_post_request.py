import pytest
import requests
from unittest.mock import patch
from src.http_post_request import send_http_post_request

class MockResponse:
    def __init__(self, status_code, json_data=None, text='', headers=None):
        self.status_code = status_code
        self._json = json_data
        self.text = text
        self.headers = headers or {}
    
    def json(self):
        if self._json is None:
            raise ValueError("No JSON data")
        return self._json

def test_send_http_post_request_success():
    # Mock a successful POST request
    with patch('requests.post') as mock_post:
        mock_response = MockResponse(
            status_code=200, 
            json_data={'message': 'success'},
            headers={'Content-Type': 'application/json'}
        )
        mock_post.return_value = mock_response

        result = send_http_post_request(
            'https://example.com/api', 
            data={'key': 'value'}, 
            headers={'Authorization': 'Bearer token'}
        )

        assert result['status_code'] == 200
        assert result['json'] == {'message': 'success'}
        assert result['headers'] == {}  # headers are mocked as empty dict

def test_send_http_post_request_no_json():
    # Mock a POST request with non-JSON response
    with patch('requests.post') as mock_post:
        mock_response = MockResponse(
            status_code=200, 
            text='Plain text response',
            headers={'Content-Type': 'text/plain'}
        )
        mock_post.return_value = mock_response

        result = send_http_post_request('https://example.com/api')

        assert result['status_code'] == 200
        assert result['json'] is None
        assert result['text'] == 'Plain text response'

def test_send_http_post_request_network_error():
    # Test network-related exceptions
    with patch('requests.post') as mock_post:
        mock_post.side_effect = requests.RequestException('Network error')

        with pytest.raises(requests.RequestException):
            send_http_post_request('https://example.com/api')

def test_send_http_post_request_default_params():
    # Test default parameters
    with patch('requests.post') as mock_post:
        mock_response = MockResponse(status_code=200)
        mock_post.return_value = mock_response

        result = send_http_post_request('https://example.com/api')

        assert result['status_code'] == 200
        mock_post.assert_called_once_with(
            'https://example.com/api', 
            json={}, 
            headers={}, 
            timeout=10
        )