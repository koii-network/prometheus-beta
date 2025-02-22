import pytest
import logging
import sys
from unittest.mock import Mock

# Import the function to test
from src.api_payload_logger import log_api_response_payload_size

def test_log_api_response_payload_size_with_content():
    """Test logging payload size for a response with .content"""
    # Create a mock response with content
    mock_response = Mock()
    mock_response.content = b'Hello, World!'
    
    # Create a mock logger
    mock_logger = Mock()
    
    # Call the function
    payload_size = log_api_response_payload_size(mock_response, mock_logger)
    
    # Assert payload size and logging
    assert payload_size == 13
    mock_logger.info.assert_called_once_with("API Response Payload Size: 13 bytes")

def test_log_api_response_payload_size_with_text():
    """Test logging payload size for a response with .text"""
    # Create a mock response with text
    mock_response = Mock()
    mock_response.text = 'Hello, World!'
    delattr(mock_response, 'content')
    
    # Create a mock logger
    mock_logger = Mock()
    
    # Call the function
    payload_size = log_api_response_payload_size(mock_response, mock_logger)
    
    # Assert payload size and logging
    assert payload_size == 13
    mock_logger.info.assert_called_once_with("API Response Payload Size: 13 bytes")

def test_log_api_response_payload_size_none_response():
    """Test error handling for None response"""
    with pytest.raises(ValueError, match="Response cannot be None"):
        log_api_response_payload_size(None)

def test_log_api_response_payload_size_invalid_response():
    """Test error handling for response without content or text"""
    mock_response = Mock()
    
    with pytest.raises(ValueError, match="Response object lacks content or text attribute"):
        log_api_response_payload_size(mock_response)

def test_log_api_response_payload_size_default_logger(caplog):
    """Test logging with default logger"""
    caplog.set_level(logging.INFO)
    
    # Create a mock response with content
    mock_response = Mock()
    mock_response.content = b'Test Payload'
    
    # Call function with default logger
    payload_size = log_api_response_payload_size(mock_response)
    
    # Assert payload size and logging
    assert payload_size == 11
    assert "API Response Payload Size: 11 bytes" in caplog.text