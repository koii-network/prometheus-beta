import logging
import pytest
from io import StringIO

from src.multiple_logger import log_multiple_values

class TestMultipleLogger:
    def setup_method(self):
        # Create a string buffer to capture log messages
        self.log_capture = StringIO()
        self.log_handler = logging.StreamHandler(self.log_capture)
        
        # Configure root logger
        logging.getLogger().addHandler(self.log_handler)
        logging.getLogger().setLevel(logging.DEBUG)

    def teardown_method(self):
        # Remove the handler and reset logging
        logging.getLogger().removeHandler(self.log_handler)
        self.log_capture.close()

    def test_log_multiple_positional_values(self):
        log_multiple_values(logging.INFO, "User", "John", "logged", "in")
        log_output = self.log_capture.getvalue().strip()
        assert "User John logged in" in log_output

    def test_log_with_kwargs(self):
        log_multiple_values(logging.DEBUG, "Processing", "data", {"count": 5, "type": "batch"})
        log_output = self.log_capture.getvalue().strip()
        assert "Processing data {'count': 5, 'type': 'batch'}" in log_output

    def test_log_with_mixed_values(self):
        log_multiple_values(logging.WARNING, "Alert:", "High", "traffic", {"level": "critical"})
        log_output = self.log_capture.getvalue().strip()
        assert "Alert: High traffic {'level': 'critical'}" in log_output

    def test_custom_logger(self):
        custom_logger = logging.getLogger('test_logger')
        custom_capture = StringIO()
        custom_handler = logging.StreamHandler(custom_capture)
        custom_logger.addHandler(custom_handler)
        custom_logger.setLevel(logging.INFO)

        log_multiple_values(logging.INFO, "Test", "message", {"key": "value"}, logger=custom_logger)
        log_output = custom_capture.getvalue().strip()
        assert "Test message {'key': 'value'}" in log_output

        custom_capture.close()
        custom_logger.removeHandler(custom_handler)

    def test_empty_values(self):
        log_multiple_values(logging.INFO)
        log_output = self.log_capture.getvalue().strip()
        assert log_output == ""

    def test_log_with_different_types(self):
        log_multiple_values(logging.INFO, "Number:", 42, "Float:", 3.14, {"boolean": True})
        log_output = self.log_capture.getvalue().strip()
        assert "Number: 42 Float: 3.14 {'boolean': True}" in log_output