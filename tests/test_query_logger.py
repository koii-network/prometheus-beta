import pytest
import logging
import time
from src.query_logger import log_query_execution_time

# Create a custom logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

def test_log_query_execution_time_success():
    mock_logger = MockLogger()
    
    @log_query_execution_time(logger=mock_logger)
    def successful_query():
        time.sleep(0.1)  # Simulate a slow query
        return "Success"
    
    result = successful_query()
    
    assert result == "Success"
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    
    assert log_type == 'info'
    assert 'successful_query' in log_message
    assert 'executed in' in log_message
    assert 'ms' in log_message

def test_log_query_execution_time_failure():
    mock_logger = MockLogger()
    
    @log_query_execution_time(logger=mock_logger)
    def failing_query():
        time.sleep(0.05)  # Simulate a partially slow query
        raise ValueError("Query failed")
    
    with pytest.raises(ValueError, match="Query failed"):
        failing_query()
    
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    
    assert log_type == 'error'
    assert 'failing_query' in log_message
    assert 'failed' in log_message
    assert 'ms' in log_message

def test_log_query_execution_time_default_logger():
    @log_query_execution_time()
    def default_logger_query():
        return "Test"
    
    result = default_logger_query()
    assert result == "Test"  # Ensure function still works with default logger