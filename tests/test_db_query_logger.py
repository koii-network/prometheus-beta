import pytest
import logging
import time
from unittest.mock import Mock, patch
from src.db_query_logger import log_query_time

# Mock database query function for testing
class MockDatabase:
    @log_query_time()
    def simple_query(self, delay=0):
        """Simulate a database query with optional delay"""
        time.sleep(delay)
        return "Query result"
    
    @log_query_time()
    def error_query(self):
        """Simulate a query that raises an exception"""
        raise ValueError("Database error")

def test_query_time_logging():
    """Test that query execution time is logged correctly"""
    # Create a mock logger
    mock_logger = Mock(spec=logging.Logger)
    
    # Create a decorator with the mock logger
    custom_log_query_time = log_query_time(mock_logger)
    
    # Create a mock database with custom logging
    class CustomMockDB:
        @custom_log_query_time
        def test_query(self, delay=0.1):
            time.sleep(delay)
            return "Test result"
    
    # Execute the query
    db = CustomMockDB()
    result = db.test_query()
    
    # Verify the result
    assert result == "Test result"
    
    # Check that info was logged
    mock_logger.info.assert_called_once()
    log_message = mock_logger.info.call_args[0][0]
    
    # Verify the log message contains the function name and execution time
    assert "test_query" in log_message
    assert "ms" in log_message

def test_query_time_error_handling():
    """Test error handling and logging for failed queries"""
    # Create a mock logger
    mock_logger = Mock(spec=logging.Logger)
    
    # Create a mock database that will raise an error
    db = MockDatabase()
    
    # Attempt to run the error query and expect an exception
    with pytest.raises(ValueError, match="Database error"):
        db.error_query()

def test_default_logger_creation():
    """Test that a default logger is created if none is provided"""
    # Use patch to ensure __name__ returns a specific value
    with patch(__name__, 'test_module'):
        # Create a mock database
        db = MockDatabase()
        
        # Run a simple query
        result = db.simple_query()
        assert result == "Query result"

def test_query_timing_accuracy():
    """Test that the timing is reasonably accurate"""
    db = MockDatabase()
    
    # Measure actual execution time
    start_time = time.perf_counter()
    db.simple_query(delay=0.2)
    actual_time = time.perf_counter() - start_time
    
    # The decorated function should take close to the specified delay
    assert 0.19 <= actual_time <= 0.25, f"Actual time: {actual_time}"