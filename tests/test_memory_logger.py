import pytest
import logging
import io
import sys
from src.memory_logger import log_memory_usage

def test_memory_logger_basic():
    """Test basic functionality of memory logger decorator."""
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    log_handler = logging.StreamHandler(log_capture)
    logger.addHandler(log_handler)
    
    # Create a test function to decorate
    @log_memory_usage(logger=logger)
    def test_function():
        # Allocate some memory
        return [x for x in range(10000)]
    
    # Call the decorated function
    result = test_function()
    
    # Get log output
    log_output = log_capture.getvalue()
    
    # Verify log output
    assert "Memory before test_function" in log_output
    assert "Memory after test_function" in log_output
    assert "Memory change for test_function" in log_output
    assert len(result) == 10000

def test_memory_logger_default_logger():
    """Test memory logger with default logger."""
    # Capture stdout 
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    @log_memory_usage()
    def simple_func():
        return "test"
    
    result = simple_func()
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Get captured output
    output = captured_output.getvalue()
    
    # Verify logging occurred
    assert "Memory before simple_func" in output
    assert "Memory after simple_func" in output
    assert result == "test"

def test_memory_logger_error_handling():
    """Test memory logger error handling."""
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    log_handler = logging.StreamHandler(log_capture)
    logger.addHandler(log_handler)
    
    @log_memory_usage(logger=logger)
    def error_func():
        raise ValueError("Test error")
    
    # Verify the error is re-raised
    with pytest.raises(ValueError, match="Test error"):
        error_func()
    
    # Verify error was logged
    log_output = log_capture.getvalue()
    assert "Error in error_func" in log_output