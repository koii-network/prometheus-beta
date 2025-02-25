import pytest
import logging
import json
from io import StringIO
from src.api_payload_logger import log_api_response_payload_size

class MockResponse:
    def __init__(self, text):
        self.text = text

def test_log_api_response_payload_size_text_response():
    # Setup logging to capture log output
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Test with text response
    text_response = MockResponse("Hello, World!")
    size = log_api_response_payload_size(text_response)
    
    # Verify size and log message
    assert size == len("Hello, World!".encode('utf-8'))
    log_output = log_capture.getvalue().strip()
    assert f"API Response Payload Size: {size} bytes" in log_output

def test_log_api_response_payload_size_dict_response():
    # Test with dictionary response
    dict_response = {"key": "value", "numbers": [1, 2, 3]}
    size = log_api_response_payload_size(dict_response)
    
    # Verify size matches string representation
    assert size == len(str(dict_response).encode('utf-8'))

def test_log_api_response_payload_size_byte_response():
    # Test with byte response
    byte_response = b"Binary data"
    size = log_api_response_payload_size(byte_response)
    
    # Verify size
    assert size == len(byte_response)

def test_log_api_response_payload_size_string_response():
    # Test with string response
    string_response = "Pure string response"
    size = log_api_response_payload_size(string_response)
    
    # Verify size
    assert size == len(string_response.encode('utf-8'))

def test_log_api_response_payload_size_invalid_type():
    # Test with unsupported type
    with pytest.raises(TypeError):
        log_api_response_payload_size(lambda x: x)

def test_log_api_response_payload_size_custom_logger():
    # Create a custom logger
    custom_logger = logging.getLogger('test_logger')
    custom_logger.setLevel(logging.INFO)
    
    # Capture log output
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    custom_logger.addHandler(handler)

    # Test with custom logger
    text_response = MockResponse("Custom logger test")
    size = log_api_response_payload_size(text_response, logger=custom_logger)
    
    # Verify size and log message
    assert size == len("Custom logger test".encode('utf-8'))
    log_output = log_capture.getvalue().strip()
    assert f"API Response Payload Size: {size} bytes" in log_output