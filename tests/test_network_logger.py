import pytest
import logging
import requests
from unittest.mock import Mock, patch
import time

from src.network_logger import NetworkResponseLogger

class TestNetworkResponseLogger:
    @pytest.fixture
    def mock_logger(self):
        """Create a mock logger for testing."""
        return Mock(spec=logging.Logger)
    
    def test_successful_request(self, mock_logger):
        """Test a successful network request logging."""
        logger = NetworkResponseLogger(logger=mock_logger)
        
        # Mock the requests.request to simulate a successful response
        with patch('requests.request') as mock_request:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.headers = {'Content-Type': 'application/json'}
            mock_request.return_value = mock_response
            
            # Simulate a request
            result = logger.log_request_time('https://example.com')
            
            # Assertions
            assert result['status_code'] == 200
            assert 'response_time' in result
            assert result['method'] == 'GET'
            
            # Verify logging was called
            mock_logger.info.assert_called_once()
    
    def test_request_with_custom_method(self, mock_logger):
        """Test request with a custom HTTP method."""
        logger = NetworkResponseLogger(logger=mock_logger)
        
        with patch('requests.request') as mock_request:
            mock_response = Mock()
            mock_response.status_code = 201
            mock_request.return_value = mock_response
            
            result = logger.log_request_time('https://example.com', method='POST')
            
            assert result['method'] == 'POST'
            assert result['status_code'] == 201
    
    def test_empty_url_raises_error(self):
        """Test that an empty URL raises a ValueError."""
        logger = NetworkResponseLogger()
        
        with pytest.raises(ValueError, match="URL cannot be empty"):
            logger.log_request_time('')
    
    def test_network_exception_handling(self, mock_logger):
        """Test handling of network-related exceptions."""
        logger = NetworkResponseLogger(logger=mock_logger)
        
        # Simulate a network request exception
        with patch('requests.request') as mock_request:
            mock_request.side_effect = requests.ConnectionError("Network error")
            
            with pytest.raises(requests.RequestException):
                logger.log_request_time('https://example.com')
            
            # Verify error was logged
            mock_logger.error.assert_called_once()
    
    def test_request_timeout(self, mock_logger):
        """Test request timeout handling."""
        logger = NetworkResponseLogger(logger=mock_logger)
        
        with patch('requests.request') as mock_request:
            mock_request.side_effect = requests.Timeout("Request timed out")
            
            with pytest.raises(requests.RequestException):
                logger.log_request_time('https://example.com', timeout=1.0)
            
            # Verify error was logged
            mock_logger.error.assert_called_once()