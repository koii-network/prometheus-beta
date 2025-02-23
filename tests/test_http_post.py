import pytest
import requests
from unittest.mock import patch
from src.http_post import send_http_post_request

def test_successful_post_request():
    # Mock a successful HTTP POST request
    with patch('requests.post') as mock_post:
        mock_response = mock_post.return_value
        mock_response.json.return_value = {"status": "success"}
        mock_response.raise_for_status.return_value = None
        mock_response.text = '{"status": "success"}'
        mock_response.status_code = 200

        result = send_http_post_request(
            'https://example.com/api', 
            data={'key': 'value'}
        )
        
        assert result == {"status": "success"}
        mock_post.assert_called_once_with(
            'https://example.com/api', 
            json={'key': 'value'}, 
            headers={'Content-Type': 'application/json'},
            timeout=10
        )

def test_empty_url_raises_error():
    with pytest.raises(ValueError, match="Invalid or empty URL"):
        send_http_post_request('')

def test_invalid_url_raises_error():
    with pytest.raises(ValueError, match="Invalid or empty URL"):
        send_http_post_request('invalid_url')

def test_request_exception_is_raised():
    # Mock a request exception
    with patch('requests.post') as mock_post:
        mock_post.side_effect = requests.RequestException("Connection error")
        
        with pytest.raises(requests.RequestException):
            send_http_post_request('https://example.com/api')

def test_empty_response_returns_empty_dict():
    # Mock a successful request with empty response
    with patch('requests.post') as mock_post:
        mock_response = mock_post.return_value
        mock_response.json.return_value = {}
        mock_response.raise_for_status.return_value = None
        mock_response.text = ''
        mock_response.status_code = 204

        result = send_http_post_request(
            'https://example.com/api'
        )
        
        assert result == {}