import logging
import pytest
from src.parameter_logger import log_parameters

# Create a custom logger for testing
class MockLogger:
    def __init__(self):
        self.logged_messages = []
    
    def info(self, message):
        self.logged_messages.append(message)

def test_log_parameters_basic():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a test function with the decorator
    @log_parameters(logger=mock_logger)
    def test_func(a, b, c=10):
        return a + b + c
    
    # Call the function
    result = test_func(1, 2, c=3)
    
    # Check the result
    assert result == 6
    
    # Check the logged message
    assert len(mock_logger.logged_messages) == 1
    assert "test_func" in mock_logger.logged_messages[0]
    assert "{'a': 1, 'b': 2, 'c': 3}" in mock_logger.logged_messages[0]

def test_log_parameters_default_arguments():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a test function with default arguments
    @log_parameters(logger=mock_logger)
    def test_func(a, b=5, c=10):
        return a + b + c
    
    # Call the function with partial arguments
    result = test_func(1)
    
    # Check the result
    assert result == 16
    
    # Check the logged message
    assert len(mock_logger.logged_messages) == 1
    assert "test_func" in mock_logger.logged_messages[0]
    assert "{'a': 1, 'b': 5, 'c': 10}" in mock_logger.logged_messages[0]

def test_log_parameters_keyword_arguments():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a test function
    @log_parameters(logger=mock_logger)
    def test_func(a, b, c):
        return a + b + c
    
    # Call the function with keyword arguments
    result = test_func(a=1, b=2, c=3)
    
    # Check the result
    assert result == 6
    
    # Check the logged message
    assert len(mock_logger.logged_messages) == 1
    assert "test_func" in mock_logger.logged_messages[0]
    assert "{'a': 1, 'b': 2, 'c': 3}" in mock_logger.logged_messages[0]

def test_log_parameters_preserves_function_metadata():
    # Create a test function
    @log_parameters()
    def test_func(a, b):
        """This is a test function."""
        return a + b
    
    # Check function metadata is preserved
    assert test_func.__name__ == "test_func"
    assert test_func.__doc__ == "This is a test function."
    
    # Verify function still works
    assert test_func(1, 2) == 3