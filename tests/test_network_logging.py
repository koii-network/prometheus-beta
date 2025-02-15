import pytest
import requests
import logging
import io
import contextlib
from unittest.mock import patch, MagicMock
import time

from src.network_logging import log_network_request_response_time

class TestNetworkLogging:
    @patch('requests.request')
    def test_successful_get_request(self, mock_request):
        # Mock a successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_request.return_value = mock_response
        
        # Patch time to control response time
        with patch('time.time', side_effect=[0, 0.5]):
            # Capture log output
            with self._capture_logs() as log_output:
                response = log_network_request_response_time('https://example.com')
                
                # Assertions
                assert response == mock_response
                assert 'Response Time: 0.5000 seconds' in log_output.getvalue()
                assert 'Status Code: 200' in log_output.getvalue()
    
    def test_invalid_http_method(self):
        with pytest.raises(ValueError, match="Invalid HTTP method"):
            log_network_request_response_time('https://example.com', method='INVALID')
    
    @patch('requests.request')
    def test_request_exception(self, mock_request):
        # Simulate a request exception
        mock_request.side_effect = requests.ConnectionError("Connection failed")
        
        with pytest.raises(requests.ConnectionError):
            with self._capture_logs() as log_output:
                log_network_request_response_time('https://example.com')
    
    @patch('requests.request')
    def test_post_request_with_data(self, mock_request):
        # Mock a successful POST request
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_request.return_value = mock_response
        
        with self._capture_logs() as log_output:
            response = log_network_request_response_time(
                'https://example.com/create', 
                method='POST', 
                json={'key': 'value'}
            )
            
            assert response == mock_response
            assert 'Method: POST' in log_output.getvalue()
    
    @staticmethod
    @contextlib.contextmanager
    def _capture_logs():
        """Capture log output for testing."""
        log_capture = io.StringIO()
        handler = logging.StreamHandler(log_capture)
        logging.getLogger().addHandler(handler)
        
        try:
            yield log_capture
        finally:
            logging.getLogger().removeHandler(handler)
            log_capture.close()