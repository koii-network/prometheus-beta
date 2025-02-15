import pytest
import logging
import time
from src.execution_timer import log_execution_time

# Configure a test logger
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

def test_log_execution_time_basic():
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def simple_function(x, y):
        time.sleep(0.1)  # Simulate some work
        return x + y
    
    result = simple_function(3, 4)
    
    # Check the result
    assert result == 7
    
    # Check logging
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    assert log_type == 'info'
    assert 'simple_function' in log_message
    assert 'executed in' in log_message
    
    # Verify execution time is around 0.1 seconds (with some tolerance)
    time_str = log_message.split('executed in ')[1].split(' seconds')[0]
    exec_time = float(time_str)
    assert 0.09 < exec_time < 0.11

def test_log_execution_time_exception():
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def error_function():
        raise ValueError("Test error")
    
    # Check that the original exception is re-raised
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check error logging
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    assert log_type == 'error'
    assert 'error_function' in log_message
    assert 'Test error' in log_message

def test_log_execution_time_default_logger():
    # Test with default logging
    @log_execution_time()
    def quick_function():
        return 42
    
    # This should not raise an exception
    result = quick_function()
    assert result == 42