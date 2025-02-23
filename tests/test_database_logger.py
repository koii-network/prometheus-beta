import logging
import time
import pytest
from src.database_logger import log_query_execution_time

# Create a custom logger for testing
class TestLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

def test_log_query_execution_time():
    test_logger = TestLogger()
    
    @log_query_execution_time(logger=test_logger)
    def mock_database_query():
        time.sleep(0.1)  # Simulate a query taking some time
        return "Query result"
    
    # Execute the query
    result = mock_database_query()
    
    # Assertions
    assert result == "Query result"
    assert len(test_logger.logs) == 1
    
    # Check log details
    log_level, log_message = test_logger.logs[0]
    assert log_level == 'info'
    assert 'Query: mock_database_query' in log_message
    assert 'Execution Time:' in log_message
    
    # Verify execution time is approximately correct
    execution_time = float(log_message.split('Execution Time:')[1].split()[0])
    assert 0.09 < execution_time < 0.11

def test_log_query_execution_time_with_error():
    test_logger = TestLogger()
    
    @log_query_execution_time(logger=test_logger)
    def mock_database_query_with_error():
        time.sleep(0.05)  # Simulate some work before error
        raise ValueError("Database connection failed")
    
    # Execute the query and expect an error
    with pytest.raises(ValueError, match="Database connection failed"):
        mock_database_query_with_error()
    
    # Assertions
    assert len(test_logger.logs) == 1
    
    # Check error log details
    log_level, log_message = test_logger.logs[0]
    assert log_level == 'error'
    assert 'Query: mock_database_query_with_error' in log_message
    assert 'Execution Time:' in log_message
    assert 'Error: Database connection failed' in log_message
    
    # Verify execution time is approximately correct
    execution_time = float(log_message.split('Execution Time:')[1].split()[0])
    assert 0.04 < execution_time < 0.06