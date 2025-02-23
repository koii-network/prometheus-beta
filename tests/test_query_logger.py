import pytest
import logging
import time
from src.query_logger import log_query_time

# Set up a specific logger for testing
test_logger = logging.getLogger('test_query_logger')
test_logger.setLevel(logging.INFO)

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.log_messages = []
    
    def info(self, msg):
        self.log_messages.append(msg)
    
    def error(self, msg):
        self.log_messages.append(msg)

def test_log_query_time_decorator():
    # Mock logging for this specific logger
    original_handlers = test_logger.handlers.copy()
    test_logger.handlers.clear()
    
    log_capture = LogCapture()
    test_logger.info = log_capture.info
    test_logger.error = log_capture.error

    # Test function with different scenarios
    @log_query_time
    def successful_query(sleep_time=0.01):
        time.sleep(sleep_time)
        return "Query result"

    @log_query_time
    def failing_query():
        raise ValueError("Query failed")

    # Test successful query logging
    result = successful_query()
    assert result == "Query result"
    assert len(log_capture.log_messages) == 1
    assert "Query 'successful_query' executed in" in log_capture.log_messages[0]
    
    # Check timing is reasonable (between 9-12 ms for 0.01s sleep)
    ms_time = float(log_capture.log_messages[0].split()[-2])
    assert 9 < ms_time < 12

    # Reset log capture
    log_capture.log_messages.clear()

    # Test error handling
    with pytest.raises(ValueError):
        failing_query()
    
    assert len(log_capture.log_messages) == 1
    assert "Error in query 'failing_query'" in log_capture.log_messages[0]

    # Test type error for non-callable
    with pytest.raises(TypeError):
        log_query_time("not a function")

    # Restore original logger
    test_logger.handlers = original_handlers