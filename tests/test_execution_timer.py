import logging
import time
import pytest
from src.execution_timer import log_execution_time

# Configure logging to capture log messages
class LogCapture:
    def __init__(self):
        self.records = []
    
    def info(self, message):
        self.records.append(('INFO', message))
    
    def error(self, message):
        self.records.append(('ERROR', message))

def test_log_execution_time():
    # Create a log capture
    log_capture = LogCapture()
    
    # Define a test function to be timed
    @log_execution_time(logger=log_capture)
    def sample_function(x, y):
        time.sleep(0.1)  # Simulate some work
        return x + y
    
    # Call the function
    result = sample_function(3, 4)
    
    # Check the result
    assert result == 7
    
    # Check log messages
    assert len(log_capture.records) == 1
    log_level, log_message = log_capture.records[0]
    
    # Verify log level and that the function name is in the message
    assert log_level == 'INFO'
    assert 'sample_function' in log_message
    assert 'executed in' in log_message

def test_log_execution_time_with_exception():
    # Create a log capture
    log_capture = LogCapture()
    
    # Define a function that raises an exception
    @log_execution_time(logger=log_capture)
    def error_function():
        raise ValueError("Test error")
    
    # Verify that the exception is still raised
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check log messages
    assert len(log_capture.records) == 1
    log_level, log_message = log_capture.records[0]
    
    # Verify error logging
    assert log_level == 'ERROR'
    assert 'error_function' in log_message
    assert 'Test error' in log_message

def test_log_execution_time_default_logger():
    # This test ensures the decorator works with default logging
    @log_execution_time()
    def simple_function():
        time.sleep(0.05)
        return "done"
    
    # Call the function
    result = simple_function()
    
    # Check the result
    assert result == "done"