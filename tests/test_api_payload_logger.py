import pytest
import logging
import sys
import io

from src.api_payload_logger import log_api_response_payload_size

class MockResponse:
    def __init__(self, content=None, text=None, json_data=None):
        self.content = content
        self.text = text
        self._json = json_data

    def json(self):
        return self._json

def test_log_payload_size_with_content():
    response = MockResponse(content=b"Sample payload")
    size = log_api_response_payload_size(response)
    assert size == 14

def test_log_payload_size_with_text():
    response = MockResponse(text="Sample text payload")
    size = log_api_response_payload_size(response)
    assert size == 19

def test_log_payload_size_with_json():
    response = MockResponse(json_data={"key": "value"})
    size = log_api_response_payload_size(response)
    assert size > 0

def test_log_payload_size_with_string():
    size = log_api_response_payload_size("Sample string")
    assert size == 13

def test_log_payload_size_with_bytes():
    size = log_api_response_payload_size(b"Sample bytes")
    assert size == 12

def test_log_payload_size_none_raises_error():
    with pytest.raises(TypeError):
        log_api_response_payload_size(None)

def test_log_payload_size_custom_logger():
    logger = logging.getLogger('test_logger')
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    size = log_api_response_payload_size("Test message", logger)
    log_output = log_capture.getvalue()
    
    assert size == 12
    assert "API Response Payload Size: 12 bytes" in log_output