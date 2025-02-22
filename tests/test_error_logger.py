import logging
import pytest
from io import StringIO
import sys
from src.error_logger import log_custom_error

def test_log_custom_error_message(caplog):
    """Test logging a custom error message"""
    caplog.set_level(logging.ERROR)
    
    log_custom_error("Test custom error message")
    
    assert len(caplog.records) == 1
    assert caplog.records[0].levelno == logging.ERROR
    assert "Test custom error message" in caplog.text

def test_log_custom_error_with_exception(caplog):
    """Test logging a custom error message with an exception"""
    caplog.set_level(logging.ERROR)
    
    try:
        raise ValueError("Sample error")
    except ValueError as e:
        log_custom_error("Error occurred", exception=e)
    
    assert len(caplog.records) >= 3  # custom message, exception type, exception details
    assert "Error occurred" in caplog.text
    assert "ValueError" in caplog.text
    assert "Sample error" in caplog.text

def test_log_custom_error_different_log_level(caplog):
    """Test logging with a different log level"""
    caplog.set_level(logging.WARNING)
    
    log_custom_error("Warning message", log_level=logging.WARNING)
    
    assert len(caplog.records) == 1
    assert caplog.records[0].levelno == logging.WARNING
    assert "Warning message" in caplog.text