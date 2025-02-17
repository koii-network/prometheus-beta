import pytest
import requests
from unittest.mock import patch
from src.http_post_request import send_http_post_request

def test_successful_post_request():
    with patch('requests.post') as mock_post:
        # Mock a successful response
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'message': 'Success'}
        mock_response.content = b'{"message": "Success"}'

        result = send_http_post_request('http://example.com', data={'key': 'value'})
        
        assert result['status_code'] == 200
        assert result['json'] == {'message': 'Success'}
        mock_post.assert_called_once_with(
            'http://example.com', 
            json={'key': 'value'}, 
            headers={'Content-Type': 'application/json'},
            timeout=10
        )

def test_post_request_with_custom_headers():
    with patch('requests.post') as mock_post:
        # Mock a successful response
        mock_response = mock_post.return_value
        mock_response.status_code = 201
        mock_response.json.return_value = {'id': 123}
        mock_response.content = b'{"id": 123}'

        result = send_http_post_request(
            'http://example.com', 
            data={'key': 'value'}, 
            headers={'Authorization': 'Bearer token'}
        )
        
        assert result['status_code'] == 201
        assert result['json'] == {'id': 123}
        mock_post.assert_called_once_with(
            'http://example.com', 
            json={'key': 'value'}, 
            headers={'Authorization': 'Bearer token'},
            timeout=10
        )

def test_request_exception():
    with patch('requests.post') as mock_post:
        # Simulate a request exception
        mock_post.side_effect = requests.RequestException('Connection error')

        result = send_http_post_request('http://example.com')
        
        assert 'error' in result
        assert result['error'] == 'Connection error'
        assert result['status_code'] is None

def test_http_error():
    with patch('requests.post') as mock_post:
        # Mock a 404 response
        mock_response = mock_post.return_value
        mock_response.raise_for_status.side_effect = requests.HTTPError('Not Found')
        mock_response.status_code = 404

        result = send_http_post_request('http://example.com')
        
        assert 'error' in result
        assert 'Not Found' in result['error']
        assert result['status_code'] == 404

def test_empty_response():
    with patch('requests.post') as mock_post:
        # Mock an empty response
        mock_response = mock_post.return_value
        mock_response.status_code = 204
        mock_response.content = b''
        mock_response.json.return_value = None

        result = send_http_post_request('http://example.com')
        
        assert result['status_code'] == 204
        assert result['json'] is None