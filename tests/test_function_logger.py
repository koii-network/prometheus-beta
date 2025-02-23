import pytest
import logging
from unittest.mock import patch
import time

from src.function_logger import log_function_execution

# Create a mock logger for testing
class MockLogger:
    def __init__(self):
        self.info_logs = []
        self.debug_logs = []
        self.error_logs = []
    
    def info(self, message):
        self.info_logs.append(message)
    
    def debug(self, message):
        self.debug_logs.append(message)
    
    def error(self, message):
        self.error_logs.append(message)
    
    def warning(self, message):
        pass  # Not used in this test

def test_log_function_execution_basic():
    """Test basic logging functionality"""
    mock_logger = MockLogger()
    
    @log_function_execution(logger=mock_logger)
    def test_func(x, y):
        return x + y
    
    result = test_func(3, 4)
    
    assert result == 7
    assert len(mock_logger.info_logs) == 3  # Start, end, and time logs
    assert "Starting execution of test_func" in mock_logger.info_logs[0]
    assert "Completed execution of test_func" in mock_logger.info_logs[1]
    assert "Execution time" in mock_logger.info_logs[2]

def test_log_function_execution_with_args():
    """Test logging with different argument types"""
    mock_logger = MockLogger()
    
    @log_function_execution(logger=mock_logger)
    def test_func_with_args(a, b=5):
        return a * b
    
    result = test_func_with_args(3, b=2)
    
    assert result == 6
    assert len(mock_logger.info_logs) == 3
    assert "Starting execution of test_func_with_args" in mock_logger.info_logs[0]

def test_log_function_execution_exception():
    """Test logging when an exception occurs"""
    mock_logger = MockLogger()
    
    @log_function_execution(logger=mock_logger)
    def test_func_with_error():
        raise ValueError("Test error")
    
    with pytest.raises(ValueError, match="Test error"):
        test_func_with_error()
    
    assert len(mock_logger.error_logs) == 1
    assert "Exception in test_func_with_error" in mock_logger.error_logs[0]

def test_log_function_execution_time():
    """Test that execution time is logged"""
    mock_logger = MockLogger()
    
    @log_function_execution(logger=mock_logger)
    def slow_func():
        time.sleep(0.1)  # Simulate a slow function
    
    slow_func()
    
    # Check that execution time was logged
    time_log = [log for log in mock_logger.info_logs if "Execution time" in log]
    assert len(time_log) == 1
    # Verify time is logged and is a float
    assert "seconds" in time_log[0]