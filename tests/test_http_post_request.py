import pytest
import requests
from unittest.mock import patch
from src.http_post_request import send_http_post_request

def test_send_http_post_request_success():
    # Mock a successful POST request
    with patch('requests.post') as mock_post:
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
        mock_response.raise_for_status.return_value = None

        result = send_http_post_request('https://example.com', data={'test': 'data'})
        
        assert result['status_code'] == 200
        assert result['json'] == {'key': 'value'}
        mock_post.assert_called_once_with(
            'https://example.com', 
            json={'test': 'data'}, 
            headers={}, 
            timeout=10
        )

def test_send_http_post_request_with_headers():
    # Test with custom headers
    with patch('requests.post') as mock_post:
        mock_response = mock_post.return_value
        mock_response.status_code = 201
        mock_response.json.return_value = {'created': True}
        mock_response.raise_for_status.return_value = None

        headers = {'Authorization': 'Bearer token123'}
        result = send_http_post_request('https://example.com', headers=headers)
        
        assert result['status_code'] == 201
        mock_post.assert_called_once_with(
            'https://example.com', 
            json=None, 
            headers=headers, 
            timeout=10
        )

def test_send_http_post_request_invalid_url():
    # Test invalid URL
    with pytest.raises(ValueError, match="Invalid URL"):
        send_http_post_request('')
        send_http_post_request(None)

def test_send_http_post_request_network_error():
    # Test network-related errors
    with patch('requests.post') as mock_post:
        mock_post.side_effect = requests.RequestException("Connection error")

        with pytest.raises(requests.RequestException, match="Error sending POST request"):
            send_http_post_request('https://example.com')

def test_send_http_post_request_http_error():
    # Test HTTP error response
    with patch('requests.post') as mock_post:
        mock_response = mock_post.return_value
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")

        with pytest.raises(requests.HTTPError):
            send_http_post_request('https://example.com')