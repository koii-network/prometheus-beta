import pytest
import logging
import time
from src.query_logger import log_query_time

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.log_messages = []
    
    def info(self, msg):
        self.log_messages.append(msg)
    
    def error(self, msg):
        self.log_messages.append(msg)

def test_log_query_time_decorator():
    # Mock logging
    original_logger = logging.getLogger(__name__)
    log_capture = LogCapture()
    logging.getLogger(__name__).info = log_capture.info
    logging.getLogger(__name__).error = log_capture.error

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
    logging.getLogger(__name__).info = original_logger.info
    logging.getLogger(__name__).error = original_logger.error