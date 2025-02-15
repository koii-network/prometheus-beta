import pytest
import logging
import time
from src.database_query_logger import log_query_execution_time

# Configure logging for tests
logging.basicConfig(level=logging.INFO)

class MockLogger:
    def __init__(self):
        self.info_messages = []
        self.error_messages = []
    
    def info(self, message):
        self.info_messages.append(message)
    
    def error(self, message):
        self.error_messages.append(message)

def test_log_query_execution_time():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a mock database query function with the decorator
    @log_query_execution_time(logger=mock_logger)
    def mock_query(delay=0):
        time.sleep(delay)  # Simulate query execution time
        return "Query result"
    
    # Test normal execution
    result = mock_query(0.1)  # 100 ms delay
    
    # Check result
    assert result == "Query result"
    
    # Check logging
    assert len(mock_logger.info_messages) == 1
    log_message = mock_logger.info_messages[0]
    assert "Query mock_query execution time:" in log_message
    
    # Check execution time logging (around 100 ms)
    time_str = log_message.split(":")[-1].strip()[:-3]  # Extract time value
    assert float(time_str) >= 100 and float(time_str) < 110

def test_log_query_execution_with_exception():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a mock query function that raises an exception
    @log_query_execution_time(logger=mock_logger)
    def query_with_error():
        raise ValueError("Database connection error")
    
    # Test exception handling
    with pytest.raises(ValueError, match="Database connection error"):
        query_with_error()
    
    # Check error logging
    assert len(mock_logger.error_messages) == 1
    assert "Error in query query_with_error:" in mock_logger.error_messages[0]