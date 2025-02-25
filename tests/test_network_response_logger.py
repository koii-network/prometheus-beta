import pytest
import requests
import logging
from unittest.mock import patch
from src.network_response_logger import log_network_request_response_time

def test_successful_get_request():
    """Test a successful GET request with response time logging."""
    with patch('requests.request') as mock_request:
        # Mock a successful response
        mock_response = mock_request.return_value
        mock_response.status_code = 200
        mock_response.content = b'Test Content'

        result = log_network_request_response_time('https://example.com')
        
        # Verify response details
        assert result['url'] == 'https://example.com'
        assert result['method'] == 'GET'
        assert result['status_code'] == 200
        assert 'response_time' in result
        assert result['response_length'] == 12

def test_empty_url_raises_error():
    """Test that an empty URL raises a ValueError."""
    with pytest.raises(ValueError, match="URL cannot be empty"):
        log_network_request_response_time('')

def test_request_with_custom_params():
    """Test request with custom method, headers, and params."""
    with patch('requests.request') as mock_request:
        mock_response = mock_request.return_value
        mock_response.status_code = 201
        mock_response.content = b'Created'

        headers = {'Authorization': 'Bearer token'}
        params = {'key': 'value'}

        result = log_network_request_response_time(
            'https://example.com/create', 
            method='POST', 
            headers=headers, 
            params=params
        )

        assert result['url'] == 'https://example.com/create'
        assert result['method'] == 'POST'
        assert result['status_code'] == 201

def test_network_exception():
    """Test handling of network-related exceptions."""
    with patch('requests.request', side_effect=requests.ConnectionError("Network Error")):
        with pytest.raises(requests.ConnectionError):
            log_network_request_response_time('https://example.com')

def test_response_time_measurement():
    """Test that response time is being measured accurately."""
    with patch('requests.request') as mock_request:
        mock_response = mock_request.return_value
        mock_response.status_code = 200
        mock_response.content = b'Test'

        result = log_network_request_response_time('https://example.com')
        
        # Check that response_time exists and is a positive float
        assert isinstance(result['response_time'], float)
        assert result['response_time'] >= 0