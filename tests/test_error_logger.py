import logging
import os
import pytest
from src.error_logger import log_custom_error

def test_log_custom_error_with_no_error():
    # Ensure no exception is raised when logging without an error
    try:
        log_custom_error("Test log message")
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")

def test_log_custom_error_with_exception():
    # Test logging with an exception
    try:
        raise ValueError("Test error")
    except ValueError as e:
        try:
            log_custom_error("An error occurred", error=e)
        except Exception as log_error:
            pytest.fail(f"Unexpected logging error: {log_error}")

def test_log_file_creation():
    # Ensure error.log file is created
    if os.path.exists('error.log'):
        os.remove('error.log')
    
    # Trigger a log
    log_custom_error("Test log for file creation")
    
    # Check if log file was created
    assert os.path.exists('error.log'), "Error log file was not created"

def test_different_log_levels():
    # Test different log levels
    log_levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
    
    for level in log_levels:
        try:
            log_custom_error(f"Test message at {logging.getLevelName(level)} level", log_level=level)
        except Exception as e:
            pytest.fail(f"Failed to log at {logging.getLevelName(level)} level: {e}")