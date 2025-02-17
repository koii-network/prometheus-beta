import pytest
import logging
import sys
from unittest.mock import Mock

# Import the function to test
sys.path.append('.')
from src.api_payload_logger import log_api_response_payload_size

class MockResponse:
    def __init__(self, content=None, text=None):
        self.content = content or b''
        self.text = text or ''

def test_log_api_response_payload_size_with_content():
    # Test with content
    mock_response = MockResponse(content=b'Hello, World!')
    mock_logger = Mock(spec=logging.Logger)
    
    size = log_api_response_payload_size(mock_response, mock_logger)
    
    assert size == 13
    mock_logger.info.assert_called_once_with("API Response Payload Size: 13 bytes")

def test_log_api_response_payload_size_with_text():
    # Test with text
    mock_response = MockResponse(text='Hello, World!')
    mock_logger = Mock(spec=logging.Logger)
    
    size = log_api_response_payload_size(mock_response, mock_logger)
    
    assert size == 13
    mock_logger.info.assert_called_once_with("API Response Payload Size: 13 bytes")

def test_log_api_response_payload_size_none_raises_error():
    # Test None response raises TypeError
    with pytest.raises(TypeError, match="Response cannot be None"):
        log_api_response_payload_size(None)

def test_log_api_response_payload_size_unsupported_raises_error():
    # Test unsupported response type raises ValueError
    unsupported_response = object()
    with pytest.raises(ValueError, match="Cannot determine payload size"):
        log_api_response_payload_size(unsupported_response)

def test_log_api_response_payload_size_empty_payload():
    # Test empty payload
    mock_response = MockResponse(content=b'')
    mock_logger = Mock(spec=logging.Logger)
    
    size = log_api_response_payload_size(mock_response, mock_logger)
    
    assert size == 0
    mock_logger.info.assert_called_once_with("API Response Payload Size: 0 bytes")