import pytest
import logging
from io import StringIO
import sys
from src.multi_logger import log_multiple

class TestMultiLogger:
    def setup_method(self):
        # Redirect logging to a string buffer for testing
        self.log_capture = StringIO()
        logging.basicConfig(stream=self.log_capture, level=logging.DEBUG, 
                            format='%(levelname)s:%(message)s')

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
        assert log_output.endswith('')

    def teardown_method(self):
        # Close the log capture
        self.log_capture.close()