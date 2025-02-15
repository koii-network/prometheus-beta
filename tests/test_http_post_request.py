import pytest
import requests
from unittest.mock import patch
from src.http_post_request import send_http_post_request

def test_send_http_post_request_success():
    # Mock successful POST request
    with patch('requests.post') as mock_post:
        # Setup mock response
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.text = '{"key": "value"}'
        mock_response.json.return_value = {"key": "value"}
        mock_response.headers = {'Content-Type': 'application/json'}

        # Call the function
        result = send_http_post_request('https://example.com/api', data={'test': 'data'})

        # Assertions
        assert result['status_code'] == 200
        assert result['json'] == {"key": "value"}
        assert result['text'] == '{"key": "value"}'
        assert 'Content-Type' in result['headers']

def test_send_http_post_request_invalid_url():
    # Test invalid URL
    with pytest.raises(ValueError):
        send_http_post_request('')
    with pytest.raises(ValueError):
        send_http_post_request(None)

def test_send_http_post_request_network_error():
    # Mock network error
    with patch('requests.post') as mock_post:
        mock_post.side_effect = requests.RequestException('Network error')

        with pytest.raises(requests.RequestException):
            send_http_post_request('https://example.com/api')

def test_send_http_post_request_http_error():
    # Mock HTTP error response
    with patch('requests.post') as mock_post:
        mock_response = mock_post.return_value
        mock_response.raise_for_status.side_effect = requests.HTTPError('HTTP Error')

        with pytest.raises(requests.HTTPError):
            send_http_post_request('https://example.com/api')

def test_send_http_post_request_custom_headers():
    # Test custom headers
    with patch('requests.post') as mock_post:
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.text = 'Success'
        mock_response.json.return_value = None

        result = send_http_post_request(
            'https://example.com/api', 
            data={'test': 'data'}, 
            headers={'Authorization': 'Bearer token'}
        )

        # Verify the function was called with custom headers
        mock_post.assert_called_once_with(
            'https://example.com/api', 
            json={'test': 'data'}, 
            headers={'Authorization': 'Bearer token'},
            timeout=10
        )

def test_send_http_post_request_no_json_response():
    # Test response without JSON
    with patch('requests.post') as mock_post:
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.text = 'Not JSON'
        mock_response.json.side_effect = ValueError('No JSON')

        result = send_http_post_request('https://example.com/api')

        assert result['json'] is None
        assert result['text'] == 'Not JSON'