import pytest
import time
import logging
from io import StringIO
from src.execution_timer import log_execution_time

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.log_output = StringIO()
        self.log_handler = logging.StreamHandler(self.log_output)
        
    def get_logs(self):
        return self.log_output.getvalue()

@log_execution_time
def simple_function(delay=0):
    """A simple function to test execution time logging."""
    time.sleep(delay)
    return "Function completed"

@log_execution_time
def error_function():
    """A function that raises an exception."""
    raise ValueError("Test error")

def test_execution_time_logging():
    # Set up log capture
    log_capture = LogCapture()
    logger = logging.getLogger()
    logger.addHandler(log_capture.log_handler)
    logger.setLevel(logging.INFO)
    
    # Call function with a known delay
    result = simple_function(0.1)
    
    # Check return value
    assert result == "Function completed"
    
    # Check log messages
    log_messages = log_capture.get_logs()
    assert "executed in" in log_messages
    
    # Check the logged time is close to the expected delay
    logged_time = float(log_messages.split()[-2])
    assert 0.09 < logged_time < 0.11, f"Unexpected execution time: {logged_time}"

def test_error_handling():
    # Set up log capture
    log_capture = LogCapture()
    logger = logging.getLogger()
    logger.addHandler(log_capture.log_handler)
    logger.setLevel(logging.INFO)
    
    # Verify that the error is raised and logged
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check log messages
    log_messages = log_capture.get_logs()
    assert "Error in function" in log_messages
    assert "error_function" in log_messages