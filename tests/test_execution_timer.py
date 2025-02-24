import pytest
import time
import logging
from src.execution_timer import log_execution_time

# Create a mock logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

def test_log_execution_time_basic():
    """Test basic execution time logging with print"""
    @log_execution_time()
    def simple_function():
        time.sleep(0.1)  # Simulate some work
    
    simple_function()  # This should print execution time

def test_log_execution_time_with_logger():
    """Test execution time logging with a custom logger"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def another_function():
        time.sleep(0.2)  # Simulate some work
    
    another_function()
    
    # Check that a log was created
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    assert log_type == 'info'
    assert 'another_function' in log_message
    assert 'took' in log_message

def test_log_execution_time_with_arguments():
    """Test execution time logging with a function that takes arguments"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def function_with_args(a, b):
        time.sleep(0.1)
        return a + b
    
    result = function_with_args(3, 4)
    assert result == 7
    
    # Check that a log was created
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    assert log_type == 'info'

def test_log_execution_time_exception():
    """Test exception handling in execution time logging"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def function_with_error():
        raise ValueError("Test error")
    
    with pytest.raises(ValueError):
        function_with_error()
    
    # Check that an error log was created
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    assert log_type == 'error'
    assert 'Test error' in log_message