import pytest
import time
import logging
from src.execution_timer import log_execution_time

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.log_messages = []
    
    def info(self, message):
        self.log_messages.append(('INFO', message))
    
    def error(self, message):
        self.log_messages.append(('ERROR', message))

# Temporarily replace logging
original_logging = logging.info
original_error_logging = logging.error

@log_execution_time
def sample_function(delay=0):
    """A sample function that optionally introduces a delay."""
    time.sleep(delay)
    return "Function completed"

@log_execution_time
def error_function():
    """A function that raises an exception."""
    raise ValueError("Test exception")

def test_log_execution_time_no_delay():
    log_capture = LogCapture()
    logging.info = log_capture.info
    
    result = sample_function()
    
    # Restore original logging
    logging.info = original_logging
    
    assert result == "Function completed"
    assert len(log_capture.log_messages) == 1
    log_message = log_capture.log_messages[0]
    assert log_message[0] == 'INFO'
    assert 'sample_function' in log_message[1]
    assert 'seconds to execute' in log_message[1]

def test_log_execution_time_with_delay():
    log_capture = LogCapture()
    logging.info = log_capture.info
    
    result = sample_function(0.1)
    
    # Restore original logging
    logging.info = original_logging
    
    assert result == "Function completed"
    assert len(log_capture.log_messages) == 1
    log_message = log_capture.log_messages[0]
    assert log_message[0] == 'INFO'
    assert 'sample_function' in log_message[1]
    assert 'seconds to execute' in log_message[1]
    
    # Check that the execution time is close to the delay
    time_str = log_message[1].split()[-2]
    exec_time = float(time_str)
    assert 0.09 < exec_time < 0.12  # Allow some tolerance

def test_log_execution_time_with_error():
    log_capture = LogCapture()
    logging.info = log_capture.info
    logging.error = log_capture.error
    
    with pytest.raises(ValueError, match="Test exception"):
        error_function()
    
    # Restore original logging
    logging.info = original_logging
    logging.error = original_error_logging
    
    assert len(log_capture.log_messages) == 1
    log_message = log_capture.log_messages[0]
    assert log_message[0] == 'ERROR'
    assert 'error_function' in log_message[1]
    assert 'seconds' in log_message[1]
    assert 'Test exception' in log_message[1]