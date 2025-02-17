import pytest
import logging
import json
from src.api_payload_logger import log_api_response_payload_size

class MockResponse:
    def __init__(self, text=None, content=None):
        self.text = text
        self.content = content

class TestAPIPayloadLogger:
    def setup_method(self):
        # Create a logger that captures logs
        self.log_capture = []
        self.logger = logging.getLogger('test_logger')
        self.logger.handlers = []  # Clear existing handlers
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)
        self.logger.propagate = False

    def test_log_payload_size_string(self):
        test_payload = "Hello, World!"
        size = log_api_response_payload_size(test_payload, self.logger)
        assert size == len(test_payload.encode('utf-8'))

    def test_log_payload_size_dict(self):
        test_payload = {"key": "value", "numbers": [1, 2, 3]}
        size = log_api_response_payload_size(test_payload, self.logger)
        assert size == len(json.dumps(test_payload).encode('utf-8'))

    def test_log_payload_size_mock_response(self):
        mock_response = MockResponse(text="API Response Content")
        size = log_api_response_payload_size(mock_response, self.logger)
        assert size == len("API Response Content".encode('utf-8'))

    def test_log_payload_size_bytes(self):
        test_payload = b"Binary payload"
        size = log_api_response_payload_size(test_payload, self.logger)
        assert size == len(test_payload)

    def test_log_payload_size_unsupported_type(self):
        class UnsupportedType:
            pass
        
        unsupported = UnsupportedType()
        size = log_api_response_payload_size(unsupported, self.logger)
        assert size == 0

    def test_log_payload_size_default_logger(self):
        # Test with default logger (no custom logger provided)
        test_payload = "Default logger test"
        size = log_api_response_payload_size(test_payload)
        assert size == len(test_payload.encode('utf-8'))