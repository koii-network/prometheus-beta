import logging
import time
import pytest
from src.db_query_logger import log_query_execution_time

class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

def test_log_query_execution_time():
    mock_logger = MockLogger()
    
    @log_query_execution_time(logger=mock_logger)
    def sample_query():
        time.sleep(0.1)  # Simulate a slow query
        return "Result"
    
    # Execute the query
    result = sample_query()
    
    # Check the result
    assert result == "Result"
    
    # Check logging
    assert len(mock_logger.logs) == 1
    log_level, log_message = mock_logger.logs[0]
    assert log_level == 'info'
    assert 'sample_query' in log_message
    assert 'executed in' in log_message

def test_log_query_execution_time_with_exception():
    mock_logger = MockLogger()
    
    @log_query_execution_time(logger=mock_logger)
    def failing_query():
        raise ValueError("Database error")
    
    # Execute the query and expect an exception
    with pytest.raises(ValueError, match="Database error"):
        failing_query()
    
    # Check logging
    assert len(mock_logger.logs) == 1
    log_level, log_message = mock_logger.logs[0]
    assert log_level == 'error'
    assert 'failing_query' in log_message
    assert 'failed' in log_message
    assert 'Database error' in log_message

def test_log_query_execution_time_default_logger():
    # Test with default logger
    @log_query_execution_time()
    def simple_query():
        return "Simple Result"
    
    # This should not raise any errors
    result = simple_query()
    assert result == "Simple Result"