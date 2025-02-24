import pytest
import logging
import time
from src.function_logger import log_execution_time

def test_log_execution_time_basic(caplog):
    """Test basic logging functionality"""
    caplog.set_level(logging.INFO)
    
    @log_execution_time
    def simple_function(x, y):
        return x + y
    
    result = simple_function(3, 4)
    
    assert result == 7
    
    # Check log messages
    log_records = caplog.records
    
    assert len(log_records) >= 3
    log_messages = [record.getMessage() for record in log_records]
    
    assert any("Starting execution of simple_function" in msg for msg in log_messages)
    assert any("Finished execution of simple_function" in msg for msg in log_messages)
    assert any("Execution time:" in msg for msg in log_messages)

def test_log_execution_time_with_exception(caplog):
    """Test logging behavior with exceptions"""
    caplog.set_level(logging.ERROR)
    
    @log_execution_time
    def error_function():
        raise ValueError("Test error")
    
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check log messages
    log_messages = [record.getMessage() for record in caplog.records]
    
    assert any("Exception in error_function" in msg for msg in log_messages)

def test_log_execution_time_performance(caplog):
    """Test logging performance and timing accuracy"""
    caplog.set_level(logging.INFO)
    
    @log_execution_time
    def sleep_function(duration):
        time.sleep(duration)
        return duration
    
    start_time = time.time()
    result = sleep_function(0.1)
    end_time = time.time()
    
    assert result == 0.1
    
    # Check log messages
    log_messages = [record.getMessage() for record in caplog.records]
    
    # Verify execution time log
    time_log = [msg for msg in log_messages if "Execution time:" in msg][0]
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