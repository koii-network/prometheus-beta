import pytest
import logging
import time
from src.db_query_logger import log_query_execution_time

# Create a mock logger to capture log messages
class MockLogger:
    def __init__(self):
        self.info_logs = []
        self.error_logs = []
    
    def info(self, message):
        self.info_logs.append(message)
    
    def error(self, message):
        self.error_logs.append(message)

def test_log_query_execution_time():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a mock database query function
    @log_query_execution_time(logger=mock_logger)
    def sample_query():
        time.sleep(0.1)  # Simulate query taking 100ms
        return "Query result"
    
    # Execute the query
    result = sample_query()
    
    # Assertions
    assert result == "Query result"
    assert len(mock_logger.info_logs) == 1
    assert "sample_query" in mock_logger.info_logs[0]
    assert "executed in" in mock_logger.info_logs[0]
    
    # Check if execution time is close to 100ms (with some tolerance)
    execution_time = float(mock_logger.info_logs[0].split()[-2])
    assert 90 < execution_time < 110, f"Execution time {execution_time} ms is not within expected range"

def test_log_query_execution_time_with_args():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a mock database query function with arguments
    @log_query_execution_time(logger=mock_logger)
    def parameterized_query(param1, param2):
        time.sleep(0.05)  # Simulate query taking 50ms
        return f"{param1} {param2}"
    
    # Execute the query
    result = parameterized_query("hello", "world")
    
    # Assertions
    assert result == "hello world"
    assert len(mock_logger.info_logs) == 1
    assert "parameterized_query" in mock_logger.info_logs[0]
    
    # Check if execution time is close to 50ms (with some tolerance)
    execution_time = float(mock_logger.info_logs[0].split()[-2])
    assert 40 < execution_time < 60, f"Execution time {execution_time} ms is not within expected range"

def test_log_query_execution_time_with_exception():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a mock database query function that raises an exception
    @log_query_execution_time(logger=mock_logger)
    def failing_query():
        raise ValueError("Query failed")
    
    # Execute the query and expect an exception
    with pytest.raises(ValueError, match="Query failed"):
        failing_query()
    
    # Assertions
    assert len(mock_logger.error_logs) == 1
    assert "Error in query 'failing_query'" in mock_logger.error_logs[0]
    assert "Query failed" in mock_logger.error_logs[0]