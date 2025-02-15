import logging
import pytest
from src.debug_logger import conditional_debug_log

# Configure logging to capture log messages
class LogCapture:
    def __init__(self):
        self.log_messages = []
    
    def debug(self, message):
        self.log_messages.append(message)

@conditional_debug_log()
def sample_function(x, y):
    return x + y

@conditional_debug_log(condition=False)
def sample_function_no_logging(x, y):
    return x + y

def test_conditional_debug_log_enabled():
    # Create a log capture
    log_capture = LogCapture()
    
    # Use a custom logger with our log capture
    with conditional_debug_log(logger=log_capture)(sample_function)(3, 4):
        pass
    
    # Verify log messages
    assert len(log_capture.log_messages) == 4
    assert "Entering function: sample_function" in log_capture.log_messages[0]
    assert "Args: (3, 4)" in log_capture.log_messages[1]
    assert "Exiting function: sample_function" in log_capture.log_messages[2]
    assert "Return value: 7" in log_capture.log_messages[3]

def test_conditional_debug_log_disabled():
    # Create a log capture
    log_capture = LogCapture()
    
    # Use a custom logger with our log capture and condition=False
    with conditional_debug_log(condition=False, logger=log_capture)(sample_function_no_logging)(3, 4):
        pass
    
    # Verify no log messages were generated
    assert len(log_capture.log_messages) == 0

def test_decorator_preserves_function_behavior():
    # Test that the function returns the correct result
    assert sample_function(3, 4) == 7
    assert sample_function_no_logging(3, 4) == 7