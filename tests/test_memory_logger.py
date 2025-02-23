import pytest
import logging
import sys
import os
import io

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from memory_logger import log_memory_usage

class LogCapture:
    def __init__(self):
        self.captured = []
    
    def write(self, message):
        self.captured.append(message)
    
    def flush(self):
        pass
    
    def getvalue(self):
        return '\n'.join(self.captured)

def test_log_memory_usage_basic():
    """Test that the decorator logs memory usage correctly."""
    log_capture = LogCapture()
    
    # Create a logger and add our custom handler
    logger = logging.getLogger()
    handler = logging.StreamHandler(log_capture)
    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    
    @log_memory_usage
    def test_function():
        # Simulate some memory allocation
        data = [i for i in range(10000)]
        return len(data)
    
    result = test_function()
    
    # Remove the handler
    logger.removeHandler(handler)
    
    # Get captured log messages
    log_messages = log_capture.getvalue().strip().split('\n')
    
    assert result == 10000
    assert len(log_messages) == 3
    assert "Memory before test_function" in log_messages[0]
    assert "Memory after test_function" in log_messages[1]
    assert "Memory change" in log_messages[2]

def test_log_memory_usage_error_handling():
    """Test error handling when decorator is applied incorrectly."""
    with pytest.raises(TypeError):
        log_memory_usage(42)  # Not a callable

def test_log_memory_usage_function_with_args():
    """Test decorator with function taking arguments."""
    log_capture = LogCapture()
    
    # Create a logger and add our custom handler
    logger = logging.getLogger()
    handler = logging.StreamHandler(log_capture)
    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    
    @log_memory_usage
    def test_function_with_args(a, b):
        return a + b
    
    result = test_function_with_args(10, 20)
    
    # Remove the handler
    logger.removeHandler(handler)
    
    # Get captured log messages
    log_messages = log_capture.getvalue().strip().split('\n')
    
    assert result == 30
    assert len(log_messages) == 3
    assert "Memory before test_function_with_args" in log_messages[0]

def test_log_memory_usage_exception_handling():
    """Test exception handling in decorated function."""
    log_capture = LogCapture()
    
    # Create a logger and add our custom handler
    logger = logging.getLogger()
    handler = logging.StreamHandler(log_capture)
    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.ERROR)
    
    @log_memory_usage
    def function_that_raises():
        raise ValueError("Test exception")
    
    with pytest.raises(ValueError):
        function_that_raises()
    
    # Remove the handler
    logger.removeHandler(handler)
    
    # Get captured log messages
    log_messages = log_capture.getvalue().strip().split('\n')
    
    assert "Error in function_that_raises" in log_messages[0]