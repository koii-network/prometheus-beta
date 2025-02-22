import pytest
import time
import logging
from src.database_logger import log_query_time

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.log_messages = []
    
    def info(self, message):
        self.log_messages.append(message)
    
    def error(self, message):
        self.log_messages.append(message)

@log_query_time
def mock_database_query(delay=0):
    """Simulate a database query with optional delay"""
    time.sleep(delay)
    return "Query Result"

@log_query_time
def mock_query_with_error():
    """Simulate a database query that raises an error"""
    raise ValueError("Database connection error")

def test_query_time_logging(caplog):
    """Test that query execution time is logged correctly"""
    caplog.set_level(logging.INFO)
    
    # Simulate a query with a small delay
    result = mock_database_query(0.1)
    
    # Check return value
    assert result == "Query Result"
    
    # Check log message
    log_records = [record.message for record in caplog.records]
    assert any("Query: mock_database_query" in log_record and "Execution Time:" in log_record 
               for log_record in log_records)

def test_query_time_logging_precision():
    """Test logging with different query execution times"""
    logger = LogCapture()
    
    # Temporarily replace the logger
    import src.database_logger
    src.database_logger.logger = logger
    
    # Run queries with different delays
    mock_database_query(0.05)  # 50ms delay
    mock_database_query(0.2)   # 200ms delay
    
    # Check log messages for timing details
    assert len(logger.log_messages) == 2
    for log_message in logger.log_messages:
        assert "Execution Time:" in log_message
        # Extract execution time
        time_str = log_message.split("Execution Time: ")[1].split(" ms")[0]
        execution_time = float(time_str)
        # Verify time is in milliseconds and reasonable
        assert 0 < execution_time < 1000

def test_query_error_handling():
    """Test error handling in query logging"""
    with pytest.raises(ValueError, match="Database connection error"):
        mock_query_with_error()