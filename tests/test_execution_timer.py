import pytest
import time
import logging
from src.execution_timer import log_execution_time

def test_log_execution_time_decorator(caplog):
    """
    Test the log_execution_time decorator with a simple function.
    """
    caplog.set_level(logging.INFO)

    @log_execution_time
    def sample_function(delay=0):
        time.sleep(delay)
        return "Hello, World!"

    # Test normal execution
    result = sample_function(0.1)
    assert result == "Hello, World!"
    
    # Check log message
    assert len(caplog.records) == 1
    log_record = caplog.records[0]
    assert log_record.levelname == "INFO"
    assert "sample_function" in log_record.message
    assert "executed in" in log_record.message

def test_log_execution_time_with_exception(caplog):
    """
    Test the log_execution_time decorator with a function that raises an exception.
    """
    caplog.set_level(logging.ERROR)

    @log_execution_time
    def error_function():
        raise ValueError("Test error")

    # Test exception handling
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check log message
    assert len(caplog.records) == 1
    log_record = caplog.records[0]
    assert log_record.levelname == "ERROR"
    assert "error_function" in log_record.message
    assert "raised an exception" in log_record.message

def test_log_execution_time_with_args(caplog):
    """
    Test the log_execution_time decorator with a function that takes arguments.
    """
    caplog.set_level(logging.INFO)

    @log_execution_time
    def add_numbers(a, b):
        return a + b

    result = add_numbers(3, 5)
    assert result == 8
    
    # Check log message
    assert len(caplog.records) == 1
    log_record = caplog.records[0]
    assert log_record.levelname == "INFO"
    assert "add_numbers" in log_record.message