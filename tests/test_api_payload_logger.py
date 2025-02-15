import pytest
import logging
from unittest.mock import Mock, patch
from src.api_payload_logger import log_api_response_payload_size

class MockResponse:
    def __init__(self, text=None, content=None):
        self.text = text
        self.content = content

def test_log_api_response_payload_size_with_text():
    mock_logger = Mock()
    response = MockResponse(text="Hello, World!")
    
    size = log_api_response_payload_size(response, logger=mock_logger)
    
    assert size == 13
    mock_logger.info.assert_called_once_with("API Response Payload Size: 13 bytes")

def test_log_api_response_payload_size_with_content():
    mock_logger = Mock()
    response = MockResponse(content=b"Binary Data")
    
    size = log_api_response_payload_size(response, logger=mock_logger)
    
    assert size == 11
    mock_logger.info.assert_called_once_with("API Response Payload Size: 11 bytes")

def test_log_api_response_payload_size_default_logger():
    with patch('logging.getLogger') as mock_get_logger:
        mock_logger = Mock()
        mock_get_logger.return_value = mock_logger
        
        response = MockResponse(text="Test")
        
        size = log_api_response_payload_size(response)
        
        assert size == 4
        mock_logger.info.assert_called_once_with("API Response Payload Size: 4 bytes")

def test_log_api_response_payload_size_none_response():
    with pytest.raises(ValueError, match="Response cannot be None"):
        log_api_response_payload_size(None)

def test_log_api_response_payload_size_invalid_response():
    class InvalidResponse:
        pass
    
    with pytest.raises(TypeError, match="Response must have 'text' or 'content' attribute"):
        log_api_response_payload_size(InvalidResponse())