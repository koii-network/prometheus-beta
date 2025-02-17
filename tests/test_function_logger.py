import logging
import pytest
import io
import sys

from src.function_logger import log_function_call

# Configure logging to capture log output
def setup_logging_capture():
    log_capture = io.StringIO()
    log_handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)
    return log_capture, logger

def test_log_function_call_basic():
    # Capture logging
    log_capture, logger = setup_logging_capture()
    
    # Create a test function with the decorator
    @log_function_call(logger=logger)
    def simple_function(x, y):
        return x + y
    
    # Call the function
    result = simple_function(3, 4)
    
    # Check the result
    assert result == 7
    
    # Get logged output
    log_output = log_capture.getvalue()
    
    # Verify log entries
    assert "Entering: simple_function(3, 4)" in log_output
    assert "Exiting: simple_function." in log_output
    assert "Execution time:" in log_output

def test_log_function_call_with_kwargs():
    # Capture logging
    log_capture, logger = setup_logging_capture()
    
    # Create a test function with the decorator
    @log_function_call(logger=logger)
    def function_with_kwargs(x, y=5):
        return x * y
    
    # Call the function with keyword argument
    result = function_with_kwargs(3, y=6)
    
    # Check the result
    assert result == 18
    
    # Get logged output
    log_output = log_capture.getvalue()
    
    # Verify log entries
    assert "Entering: function_with_kwargs(3, y=6)" in log_output
    assert "Exiting: function_with_kwargs." in log_output

def test_log_function_call_exception():
    # Capture logging
    log_capture, logger = setup_logging_capture()
    
    # Create a function that raises an exception
    @log_function_call(logger=logger)
    def error_function(x):
        raise ValueError("Test error")
    
    # Verify that the exception is raised
    with pytest.raises(ValueError, match="Test error"):
        error_function(10)
    
    # Get logged output
    log_output = log_capture.getvalue()
    
    # Verify log entries
    assert "Entering: error_function(10)" in log_output
    assert "Exception in error_function: Test error" in log_output