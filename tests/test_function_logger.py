import pytest
import logging
import time
from src.function_logger import log_execution_time

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.captured_logs = []
    
    def capture(self, record):
        self.captured_logs.append(record)

@pytest.fixture
def log_handler():
    """Fixture to capture log messages"""
    log_capture = LogCapture()
    handler = logging.Handler()
    handler.emit = log_capture.capture
    logger = logging.getLogger()
    logger.addHandler(handler)
    
    yield log_capture
    
    logger.removeHandler(handler)

def test_log_execution_time_basic(log_handler):
    """Test basic logging functionality"""
    @log_execution_time
    def simple_function(x, y):
        return x + y
    
    result = simple_function(3, 4)
    
    assert result == 7
    
    # Check log messages
    log_messages = [record for record in log_handler.captured_logs if record.levelno == logging.INFO]
    
    assert len(log_messages) >= 3
    assert any("Starting execution of simple_function" in msg.getMessage() for msg in log_messages)
    assert any("Finished execution of simple_function" in msg.getMessage() for msg in log_messages)
    assert any("Execution time:" in msg.getMessage() for msg in log_messages)

def test_log_execution_time_with_exception(log_handler):
    """Test logging behavior with exceptions"""
    @log_execution_time
    def error_function():
        raise ValueError("Test error")
    
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check log messages
    log_messages = log_handler.captured_logs
    
    assert any("Exception in error_function" in msg.getMessage() for msg in log_messages)

def test_log_execution_time_performance(log_handler):
    """Test logging performance and timing accuracy"""
    @log_execution_time
    def sleep_function(duration):
        time.sleep(duration)
        return duration
    
    start_time = time.time()
    result = sleep_function(0.1)
    end_time = time.time()
    
    assert result == 0.1
    
    # Check log messages
    log_messages = [record for record in log_handler.captured_logs if record.levelno == logging.INFO]
    
    # Verify execution time log
    time_log = [msg.getMessage() for msg in log_messages if "Execution time:" in msg.getMessage()][0]
    reported_time = float(time_log.split(":")[-1].strip().split()[0])
    
    # Allow small margin of error for timing
    assert abs(reported_time - 0.1) < 0.02

def test_log_execution_time_preserves_metadata():
    """Test that decorator preserves function metadata"""
    @log_execution_time
    def test_func(x, y):
        """A docstring to test metadata preservation"""
        return x + y
    
    assert test_func.__name__ == "test_func"
    assert test_func.__doc__ == "A docstring to test metadata preservation"