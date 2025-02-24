import pytest
import logging
from io import StringIO
import sys
from src.multi_logger import log_multiple

class TestMultiLogger:
    def setup_method(self):
        # Redirect logging to a string buffer for testing
        self.log_capture = StringIO()
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        
        # Remove existing handlers
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
        
        # Create a StreamHandler using the StringIO
        handler = logging.StreamHandler(self.log_capture)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(levelname)s:%(message)s')
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)

    def test_default_info_logging(self):
        log_multiple('info', 'Hello', 'World', 42)
        log_output = self.log_capture.getvalue().strip()
        assert 'INFO:Hello World 42' in log_output

    def test_different_log_levels(self):
        log_levels = ['debug', 'warning', 'error', 'critical']
        for level in log_levels:
            # Clear the log capture
            self.log_capture.truncate(0)
            self.log_capture.seek(0)
            
            # Log with different levels
            log_multiple(level, 'Test', 'Message', 123)
            log_output = self.log_capture.getvalue().strip()
            assert log_output.startswith(level.upper())

    def test_custom_separator(self):
        log_multiple('info', 'Apple', 'Banana', 'Cherry', separator='-')
        log_output = self.log_capture.getvalue().strip()
        assert 'Apple-Banana-Cherry' in log_output

    def test_mixed_type_values(self):
        log_multiple('info', 42, 'test', [1, 2, 3], {'key': 'value'})
        log_output = self.log_capture.getvalue().strip()
        assert 'INFO:42 test [1, 2, 3] {\'key\': \'value\'}' in log_output

    def test_invalid_log_level(self):
        with pytest.raises(ValueError, match="Invalid logging level"):
            log_multiple('invalid_level', 'Test')

    def test_no_values(self):
        log_multiple('info')
        log_output = self.log_capture.getvalue().strip()
        assert log_output == ''

    def teardown_method(self):
        # Close the log capture and remove handlers
        root_logger = logging.getLogger()
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
        self.log_capture.close()