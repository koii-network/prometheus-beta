import pytest
import time
from src.query_logger import log_query_time, logger

# Mock logger to capture log messages
class MockLogger:
    def __init__(self):
        self.log_messages = []
    
    def info(self, message):
        self.log_messages.append(('info', message))
    
    def error(self, message):
        self.log_messages.append(('error', message))

@log_query_time
def sample_query(duration=0.1):
    """Simulate a database query with variable execution time."""
    time.sleep(duration)
    return "Query result"

@log_query_time
def failing_query():
    """Simulate a query that raises an exception."""
    raise ValueError("Database connection error")

def test_query_logger_timing(monkeypatch):
    # Create a mock logger
    mock_logger = MockLogger()
    monkeypatch.setattr(logger, 'info', mock_logger.info)
    
    # Execute the query
    result = sample_query(0.2)
    
    # Check the result
    assert result == "Query result"
    
    # Check log message
    assert len(mock_logger.log_messages) == 1
    log_level, log_message = mock_logger.log_messages[0]
    
    assert log_level == 'info'
    assert 'sample_query' in log_message
    assert 'ms' in log_message

def test_query_logger_with_short_query(monkeypatch):
    mock_logger = MockLogger()
    monkeypatch.setattr(logger, 'info', mock_logger.info)
    
    result = sample_query(0.01)
    
    assert result == "Query result"
    assert len(mock_logger.log_messages) == 1

def test_query_logger_error_handling(monkeypatch):
    mock_logger = MockLogger()
    monkeypatch.setattr(logger, 'error', mock_logger.error)
    
    with pytest.raises(ValueError):
        failing_query()
    
    assert len(mock_logger.log_messages) == 1
    log_level, log_message = mock_logger.log_messages[0]
    
    assert log_level == 'error'
    assert 'failing_query' in log_message
    assert 'Database connection error' in log_message

def test_invalid_decorator_usage():
    with pytest.raises(TypeError):
        log_query_time(42)  # Not a callable