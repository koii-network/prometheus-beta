import pytest
import logging
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.error_logger import log_custom_error

def test_log_custom_error_without_error(caplog):
    """Test logging a custom message without an error"""
    caplog.set_level(logging.ERROR)
    
    log_custom_error("Test custom message")
    
    assert len(caplog.records) == 1
    assert caplog.records[0].message == "Test custom message"
    assert caplog.records[0].levelno == logging.ERROR

def test_log_custom_error_with_error(caplog):
    """Test logging a custom message with an error"""
    caplog.set_level(logging.ERROR)
    
    try:
        raise ValueError("Test error")
    except ValueError as e:
        log_custom_error("An error occurred", error=e)
    
    assert len(caplog.records) > 1
    assert any("Test error" in record.message for record in caplog.records)
    assert any("Error Type: ValueError" in record.message for record in caplog.records)

def test_log_custom_error_different_log_level(caplog):
    """Test logging with a different log level"""
    caplog.set_level(logging.WARNING)
    
    log_custom_error("Warning message", log_level=logging.WARNING)
    
    assert len(caplog.records) == 1
    assert caplog.records[0].message == "Warning message"
    assert caplog.records[0].levelno == logging.WARNING

def test_error_log_file_creation():
    """Test that an error log file is created"""
    log_custom_error("Log file test message")
    
    assert os.path.exists('error.log')
    
    # Optional: Clean up log file after test
    if os.path.exists('error.log'):
        os.remove('error.log')