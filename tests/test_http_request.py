import pytest
import requests
from unittest.mock import patch
from src.http_request import send_http_get_request

def test_send_http_get_request_success():
    # Mock a successful request
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = "Success response"
        mock_response.headers = {'Content-Type': 'text/plain'}
        mock_response.raise_for_status.return_value = None

        result = send_http_get_request('https://example.com')
        
        assert result['status_code'] == 200
        assert result['content'] == "Success response"
        assert 'Content-Type' in result['headers']

def test_send_http_get_request_with_params():
    # Test request with query parameters
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = "Params response"
        mock_response.headers = {}
        mock_response.raise_for_status.return_value = None

        result = send_http_get_request('https://example.com', params={'key': 'value'})
        
        mock_get.assert_called_once_with(
            'https://example.com', 
            headers=None, 
            params={'key': 'value'}, 
            timeout=10
        )

def test_send_http_get_request_empty_url():
    # Test empty URL raises ValueError
    with pytest.raises(ValueError, match="URL cannot be empty or None"):
        send_http_get_request('')

def test_send_http_get_request_network_error():
    # Test network-related errors
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.ConnectionError("Network error")

        with pytest.raises(RuntimeError, match="HTTP GET request failed"):
            send_http_get_request('https://example.com')

def test_send_http_get_request_http_error():
    # Test HTTP error responses
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")

        with pytest.raises(requests.HTTPError):
            send_http_get_request('https://example.com')