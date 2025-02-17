import pytest
import time
import logging
from src.execution_timer import log_execution_time

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.log_messages = []
    
    def handler(self, record):
        self.log_messages.append(record.getMessage())

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
    logging.getLogger().addHandler(logging.Handler())
    logging.getLogger().handlers[-1].emit = log_capture.handler
    
    # Call function with a known delay
    result = simple_function(0.1)
    
    # Check return value
    assert result == "Function completed"
    
    # Check log messages
    log_messages = log_capture.log_messages
    assert len(log_messages) > 0
    
    # Verify execution time log
    execution_time_log = [msg for msg in log_messages if "executed in" in msg]
    assert len(execution_time_log) == 1
    
    # Check the logged time is close to the expected delay
    logged_time = float(execution_time_log[0].split()[-2])
    assert 0.09 < logged_time < 0.11, f"Unexpected execution time: {logged_time}"

def test_error_handling():
    # Set up log capture
    log_capture = LogCapture()
    logging.getLogger().addHandler(logging.Handler())
    logging.getLogger().handlers[-1].emit = log_capture.handler
    
    # Verify that the error is raised and logged
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check log messages
    log_messages = log_capture.log_messages
    error_logs = [msg for msg in log_messages if "Error in function" in msg]
    assert len(error_logs) == 1
    assert "error_function" in error_logs[0]