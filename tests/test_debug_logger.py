import logging
import pytest
from src.debug_logger import conditional_debug_log

# Create a custom logger for testing
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.DEBUG)

# Capture log messages
class LogCapture:
    def __init__(self, logger):
        self.logger = logger
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.messages = []
        formatter = logging.Formatter('%(message)s')
        self.handler.setFormatter(formatter)
        self.handler.emit = lambda record: self.messages.append(record.getMessage())
        self.logger.addHandler(self.handler)
    
    def get_messages(self):
        return self.messages
    
    def clear(self):
        self.messages.clear()
    
    def __del__(self):
        self.logger.removeHandler(self.handler)

def test_debug_logging_enabled():
    """Test that debug messages are logged when condition is True."""
    log_capture = LogCapture(test_logger)
    
    @conditional_debug_log(condition=True, logger=test_logger)
    def sample_function(x, y):
        return x + y
    
    result = sample_function(3, 4)
    
    assert result == 7
    assert len(log_capture.get_messages()) == 2
    assert "Calling sample_function with args: (3, 4)" in log_capture.get_messages()[0]
    assert "sample_function returned: 7" in log_capture.get_messages()[1]

def test_debug_logging_disabled():
    """Test that no debug messages are logged when condition is False."""
    log_capture = LogCapture(test_logger)
    
    @conditional_debug_log(condition=False, logger=test_logger)
    def sample_function(x, y):
        return x + y
    
    result = sample_function(3, 4)
    
    assert result == 7
    assert len(log_capture.get_messages()) == 0

def test_debug_logging_default_logger():
    """Test logging with default root logger."""
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    
    log_capture = LogCapture(root_logger)
    
    @conditional_debug_log()
    def sample_function(x, y):
        return x + y
    
    result = sample_function(3, 4)
    
    assert result == 7
    assert len(log_capture.get_messages()) == 2

def test_debug_logging_with_no_arguments():
    """Test logging for a function with no arguments."""
    log_capture = LogCapture(test_logger)
    
    @conditional_debug_log(condition=True, logger=test_logger)
    def sample_function():
        return 42
    
    result = sample_function()
    
    assert result == 42
    assert len(log_capture.get_messages()) == 2
    assert "Calling sample_function with args: (), kwargs: {}" in log_capture.get_messages()[0]
    assert "sample_function returned: 42" in log_capture.get_messages()[1]