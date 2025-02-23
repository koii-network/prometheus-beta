import pytest
import time
import logging
from src.execution_timer import log_execution_time

# Mock logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

def test_log_execution_time_default():
    """Test logging with default print mechanism"""
    @log_execution_time()
    def simple_func():
        time.sleep(0.1)  # Simulate some work
    
    simple_func()  # Should print execution time

def test_log_execution_time_with_logger():
    """Test logging with a custom logger"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def another_func(x, y):
        time.sleep(0.05)  # Simulate some work
        return x + y
    
    result = another_func(3, 4)
    assert result == 7
    
    # Check that a log was created
    assert len(mock_logger.logs) == 1
    log_level, log_message = mock_logger.logs[0]
    assert log_level == 'info'
    assert 'another_func' in log_message
    assert 'seconds' in log_message

def test_log_execution_time_with_exception():
    """Test logging when an exception occurs"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def error_func():
        raise ValueError("Test error")
    
    with pytest.raises(ValueError):
        error_func()
    
    # Check that an error log was created
    assert len(mock_logger.logs) == 1
    log_level, log_message = mock_logger.logs[0]
    assert log_level == 'error'
    assert 'error_func' in log_message
    assert 'Test error' in log_message

def test_log_execution_time_with_args():
    """Test logging with different argument types"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def func_with_args(a, b=2):
        time.sleep(0.01)
        return a * b
    
    result = func_with_args(3, b=4)
    assert result == 12
    
    # Check log was created
    assert len(mock_logger.logs) == 1
    log_level, log_message = mock_logger.logs[0]
    assert log_level == 'info'
    assert 'func_with_args' in log_message