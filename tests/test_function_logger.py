import logging
import pytest
from src.function_logger import log_function_call

# Create a custom logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

def test_log_function_call_basic():
    mock_logger = MockLogger()
    
    @log_function_call(logger=mock_logger)
    def test_func(x, y):
        return x + y
    
    # Call the function
    result = test_func(3, 4)
    
    # Assert the result
    assert result == 7
    
    # Check log entries
    assert len(mock_logger.logs) == 2
    
    # Check entry log
    assert mock_logger.logs[0][0] == 'info'
    assert 'Entering function: test_func' in mock_logger.logs[0][1]
    assert '(3, 4)' in mock_logger.logs[0][1]
    
    # Check exit log
    assert mock_logger.logs[1][0] == 'info'
    assert 'Exiting function: test_func' in mock_logger.logs[1][1]

def test_log_function_call_with_exception():
    mock_logger = MockLogger()
    
    @log_function_call(logger=mock_logger)
    def error_func():
        raise ValueError("Test error")
    
    # Attempt to call function and expect exception
    with pytest.raises(ValueError, match="Test error"):
        error_func()
    
    # Check log entries
    assert len(mock_logger.logs) == 2
    
    # Check entry log
    assert mock_logger.logs[0][0] == 'info'
    assert 'Entering function: error_func' in mock_logger.logs[0][1]
    
    # Check error log
    assert mock_logger.logs[1][0] == 'error'
    assert 'Exception in error_func' in mock_logger.logs[1][1]

def test_log_function_call_with_kwargs():
    mock_logger = MockLogger()
    
    @log_function_call(logger=mock_logger)
    def kwargs_func(x, y=0):
        return x + y
    
    # Call the function with kwargs
    result = kwargs_func(3, y=5)
    
    # Assert the result
    assert result == 8
    
    # Check log entries
    assert len(mock_logger.logs) == 2
    
    # Check entry log
    assert mock_logger.logs[0][0] == 'info'
    assert 'Entering function: kwargs_func' in mock_logger.logs[0][1]
    assert 'x=3, y=5' in mock_logger.logs[0][1]