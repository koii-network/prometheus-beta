import logging
import pytest
import memory_profiler
from src.memory_logger import log_memory_usage

# Setup a mock logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(message)

def test_log_memory_usage_default():
    # Function to test memory logging with default (print) logging
    @log_memory_usage()
    def sample_function(x):
        # Allocate some memory
        large_list = [i for i in range(10000)]
        return x * 2
    
    # Call the function and check it works
    result = sample_function(5)
    assert result == 10

def test_log_memory_usage_with_custom_logger():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Decorator with custom logger
    @log_memory_usage(logger=mock_logger)
    def another_sample_function(x):
        # Allocate some memory
        large_dict = {i: i*2 for i in range(10000)}
        return x + 1
    
    # Call the function
    result = another_sample_function(7)
    assert result == 8
    
    # Check logs were captured
    assert len(mock_logger.logs) == 3
    assert "Memory before another_sample_function" in mock_logger.logs[0]
    assert "Memory after another_sample_function" in mock_logger.logs[1]
    assert "Memory change" in mock_logger.logs[2]

def test_log_memory_usage_preserves_function_metadata():
    @log_memory_usage()
    def test_func(x, y):
        """Test function docstring"""
        return x + y
    
    assert test_func.__name__ == 'test_func'
    assert test_func.__doc__ == 'Test function docstring'
    
    # Verify functionality is preserved
    assert test_func(3, 4) == 7