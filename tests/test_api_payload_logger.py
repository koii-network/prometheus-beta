import pytest
import logging
from unittest.mock import Mock

from src.api_payload_logger import log_api_response_payload_size

class MockResponse:
    def __init__(self, text=None, content=None, headers=None):
        self.text = text or ""
        self.content = content or b""
        self.headers = headers or {}

def test_log_api_response_payload_size_text():
    response = MockResponse(text="Hello, world!")
    mock_logger = Mock()
    
    size = log_api_response_payload_size(response, logger=mock_logger)
    
    assert size == len("Hello, world!".encode('utf-8'))
    mock_logger.info.assert_called_with(f"API Response Payload Size: {size} bytes")

def test_log_api_response_payload_size_headers():
    response = MockResponse(headers={'Content-Length': '42'})
    mock_logger = Mock()
    
    size = log_api_response_payload_size(response, logger=mock_logger)
    
    assert size == 42
    mock_logger.info.assert_called_with("API Response Payload Size: 42 bytes (from headers)")

def test_log_api_response_payload_size_empty():
    response = MockResponse()
    mock_logger = Mock()
    
    size = log_api_response_payload_size(response, logger=mock_logger)
    
    assert size == 0
    mock_logger.info.assert_called_with("API Response Payload Size: 0 bytes")

def test_log_api_response_payload_size_none():
    with pytest.raises(ValueError, match="Response cannot be None"):
        log_api_response_payload_size(None)

def test_log_api_response_payload_size_default_logger(caplog):
    caplog.set_level(logging.INFO)
    response = MockResponse(text="Test payload")
    
    size = log_api_response_payload_size(response)
    
    assert size == len("Test payload".encode('utf-8'))
    assert f"API Response Payload Size: {size} bytes" in caplog.text