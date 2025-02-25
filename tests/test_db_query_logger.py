import logging
import time
import pytest
from src.db_query_logger import log_query_execution_time

# Mock database-like functions for testing
class MockLogger:
    def __init__(self):
        self.logs = []

    def info(self, message):
        self.logs.append(('info', message))

    def error(self, message):
        self.logs.append(('error', message))

def test_log_query_execution_time_success():
    mock_logger = MockLogger()

    @log_query_execution_time(mock_logger)
    def mock_database_query():
        time.sleep(0.1)  # Simulate a query taking 100ms
        return "Query result"

    result = mock_database_query()
    
    assert result == "Query result"
    assert len(mock_logger.logs) == 1
    assert mock_logger.logs[0][0] == 'info'
    assert 'mock_database_query' in mock_logger.logs[0][1]
    assert 'executed in' in mock_logger.logs[0][1]

def test_log_query_execution_time_error():
    mock_logger = MockLogger()

    @log_query_execution_time(mock_logger)
    def mock_database_query_with_error():
        time.sleep(0.05)  # Simulate some execution time
        raise ValueError("Database connection error")

    with pytest.raises(ValueError, match="Database connection error"):
        mock_database_query_with_error()

    assert len(mock_logger.logs) == 1
    assert mock_logger.logs[0][0] == 'error'
    assert 'mock_database_query_with_error' in mock_logger.logs[0][1]
    assert 'failed' in mock_logger.logs[0][1]

def test_log_query_execution_time_default_logger():
    # This test ensures the decorator works with default logging
    @log_query_execution_time()
    def simple_query():
        return "Simple result"

    result = simple_query()
    assert result == "Simple result"

def test_log_query_execution_time_millisecond_precision():
    mock_logger = MockLogger()

    @log_query_execution_time(mock_logger)
    def quick_query():
        time.sleep(0.0001)  # Very short query
        return "Quick result"

    result = quick_query()
    
    assert result == "Quick result"
    assert len(mock_logger.logs) == 1
    assert 'in ' in mock_logger.logs[0][1]  # Ensure timing is logged
    assert 'ms' in mock_logger.logs[0][1]   # Ensure milliseconds are used