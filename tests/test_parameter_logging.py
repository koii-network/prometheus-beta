import logging
import pytest
from src.parameter_logging import log_parameters

# Create a custom logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(message)

def test_log_parameters_default_arguments():
    # Create mock logger
    mock_logger = MockLogger()
    
    # Create a sample function with the decorator
    @log_parameters(logger=mock_logger)
    def sample_function(a, b=10, c='test'):
        return a + b
    
    # Call the function
    result = sample_function(5)
    
    # Check the result
    assert result == 15
    
    # Check the logged message
    assert len(mock_logger.logs) == 1
    assert "Calling sample_function(a=5, b=10, c='test')" in mock_logger.logs[0]

def test_log_parameters_with_kwargs():
    # Create mock logger
    mock_logger = MockLogger()
    
    # Create a sample function with the decorator
    @log_parameters(logger=mock_logger)
    def another_function(x, y, z=None):
        return x * y
    
    # Call the function with keyword arguments
    result = another_function(x=3, y=4, z='optional')
    
    # Check the result
    assert result == 12
    
    # Check the logged message
    assert len(mock_logger.logs) == 1
    assert "Calling another_function(x=3, y=4, z='optional')" in mock_logger.logs[0]

def test_log_parameters_no_logger():
    # Test with default root logger
    @log_parameters()
    def simple_function(val):
        return val * 2
    
    # Call the function (this will use root logger)
    result = simple_function(7)
    
    # Check the result
    assert result == 14