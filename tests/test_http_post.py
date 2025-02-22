import pytest
import requests
from unittest.mock import patch
from src.http_post import send_http_post_request

class MockResponse:
    def __init__(self, status_code=200, headers=None, json_data=None):
        self.status_code = status_code
        self.headers = headers or {}
        self._json_data = json_data or {}
        self.text = str(json_data) if json_data else ''

    def json(self):
        return self._json_data

    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.HTTPError(f"HTTP Error: {self.status_code}")

def test_send_http_post_request_success():
    with patch('requests.post') as mock_post:
        # Mock a successful response
        mock_response = MockResponse(
            status_code=200, 
            headers={'Content-Type': 'application/json'},
            json_data={'message': 'success'}
        )
        mock_post.return_value = mock_response

        result = send_http_post_request(
            'https://example.com/api', 
            data={'key': 'value'}, 
            headers={'Authorization': 'Bearer token'}
        )

        # Verify the result structure
        assert result['status_code'] == 200
        assert result['body'] == {'message': 'success'}
        assert 'Content-Type' in result['headers']

def test_send_http_post_request_invalid_url():
    # Test invalid URL
    with pytest.raises(ValueError):
        send_http_post_request('')
    with pytest.raises(ValueError):
        send_http_post_request(None)

def test_send_http_post_request_network_error():
    with patch('requests.post') as mock_post:
        # Simulate a network error
        mock_post.side_effect = requests.RequestException('Network Error')

        with pytest.raises(requests.RequestException):
            send_http_post_request('https://example.com/api')

def test_send_http_post_request_http_error():
    with patch('requests.post') as mock_post:
        # Mock a 404 error response
        mock_response = MockResponse(status_code=404)
        mock_post.return_value = mock_response

        with pytest.raises(requests.HTTPError):
            send_http_post_request('https://example.com/api')

def test_send_http_post_request_empty_response():
    with patch('requests.post') as mock_post:
        # Mock an empty response
        mock_response = MockResponse(status_code=204)
        mock_post.return_value = mock_response

        result = send_http_post_request('https://example.com/api')
        assert result['body'] == {}
        assert result['status_code'] == 204