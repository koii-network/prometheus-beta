import pytest
import logging
import os
from src.error_logger import log_custom_error

def test_log_custom_message():
    """Test logging a simple custom message"""
    assert log_custom_error("Test custom message") == True

def test_log_with_error():
    """Test logging with an error object"""
    try:
        raise ValueError("Test error")
    except ValueError as e:
        assert log_custom_error("Error occurred", error=e) == True

def test_log_file_creation():
    """Test that the log file is created"""
    log_custom_error("File creation test")
    assert os.path.exists('error.log')

def test_log_levels():
    """Test different log levels"""
    assert log_custom_error("Warning message", log_level=logging.WARNING) == True
    assert log_custom_error("Critical message", log_level=logging.CRITICAL) == True

def test_invalid_log_level():
    """Test handling of invalid log level"""
    with pytest.raises(ValueError):
        log_custom_error("Invalid level test", log_level=999)