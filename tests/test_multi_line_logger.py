import logging
import pytest
from src.multi_line_logger import log_multiline

# Setup logging to capture log messages
class LogCapture:
    def __init__(self):
        self.log_records = []
        self.handler = logging.Handler()
        self.handler.emit = self._custom_emit

    def _custom_emit(self, record):
        self.log_records.append(record)

def test_log_multiline_default():
    """Test default logging behavior"""
    log_capture = LogCapture()
    logger = logging.getLogger()
    logger.addHandler(log_capture.handler)
    
    message = "Test multi-line logging"
    sep_line = log_multiline(message)
    
    assert len(log_capture.log_records) == 3
    assert log_capture.log_records[0].msg == '*' * 40
    assert log_capture.log_records[1].msg == message
    assert log_capture.log_records[2].msg == '*' * 40
    assert sep_line == '*' * 40

def test_log_multiline_custom_params():
    """Test logging with custom separator and length"""
    log_capture = LogCapture()
    logger = logging.getLogger()
    logger.addHandler(log_capture.handler)
    
    message = "Custom logging test"
    sep_line = log_multiline(message, 
                              level=logging.WARNING, 
                              separator='-', 
                              separator_length=20)
    
    assert len(log_capture.log_records) == 3
    assert log_capture.log_records[0].msg == '-' * 20
    assert log_capture.log_records[1].msg == message
    assert log_capture.log_records[2].msg == '-' * 20
    assert log_capture.log_records[0].levelno == logging.WARNING
    assert sep_line == '-' * 20

def test_log_multiline_error_cases():
    """Test error handling for invalid inputs"""
    # Non-string message
    with pytest.raises(TypeError, match="Message must be a string"):
        log_multiline(123)
    
    # Non-string separator
    with pytest.raises(TypeError, match="Separator must be a string"):
        log_multiline("Test", separator=123)
    
    # Empty separator
    with pytest.raises(ValueError, match="Separator cannot be an empty string"):
        log_multiline("Test", separator='')
    
    # Invalid separator length
    with pytest.raises(ValueError, match="Separator length must be at least 1"):
        log_multiline("Test", separator_length=0)