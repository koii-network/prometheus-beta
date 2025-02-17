import logging
import pytest
from io import StringIO
import json

from src.json_logger import log_json

class TestJsonLogger:
    def setup_method(self):
        # Create a logger with a string buffer for capturing log output
        self.log_capture = StringIO()
        self.logger = logging.getLogger('test_logger')
        self.logger.setLevel(logging.DEBUG)
        
        # Remove existing handlers
        self.logger.handlers.clear()
        
        # Create a stream handler that writes to our string buffer
        handler = logging.StreamHandler(self.log_capture)
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(handler)

    def test_log_simple_json(self):
        # Test logging a simple JSON object
        test_obj = {"name": "John", "age": 30}
        log_json(self.logger, logging.INFO, test_obj)
        
        log_output = self.log_capture.getvalue().strip()
        assert json.dumps(test_obj, indent=2) in log_output

    def test_log_with_message(self):
        # Test logging with an additional message
        test_obj = {"status": "active", "id": 123}
        log_json(self.logger, logging.DEBUG, test_obj, "User details:")
        
        log_output = self.log_capture.getvalue().strip()
        assert "User details:" in log_output
        assert json.dumps(test_obj, indent=2) in log_output

    def test_log_nested_json(self):
        # Test logging a nested JSON object
        test_obj = {
            "user": {
                "name": "Alice",
                "details": {
                    "email": "alice@example.com",
                    "active": True
                }
            }
        }
        log_json(self.logger, logging.INFO, test_obj)
        
        log_output = self.log_capture.getvalue().strip()
        assert json.dumps(test_obj, indent=2) in log_output

    def test_non_serializable_json(self):
        # Test attempting to log a non-JSON-serializable object
        non_serializable_obj = set([1, 2, 3])
        
        with pytest.raises(TypeError):
            log_json(self.logger, logging.ERROR, non_serializable_obj)

    def test_log_empty_json(self):
        # Test logging an empty dictionary
        test_obj = {}
        log_json(self.logger, logging.INFO, test_obj)
        
        log_output = self.log_capture.getvalue().strip()
        assert json.dumps(test_obj, indent=2) in log_output