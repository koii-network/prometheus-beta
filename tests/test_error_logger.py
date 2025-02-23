import pytest
import logging
import sys
from io import StringIO
from src.error_logger import log_custom_error

def test_log_custom_error_message():
    """Test basic error message logging"""
    # Create a StringIO to capture log output
    captured_output = StringIO()

    log_custom_error("Test error message", log_stream=captured_output)
    output = captured_output.getvalue()
    
    assert "Test error message" in output
    assert "ERROR" in output

def test_log_custom_error_with_exception():
    """Test logging with an exception"""
    # Create a StringIO to capture log output
    captured_output = StringIO()

    try:
        raise ValueError("Test exception")
    except ValueError as e:
        log_custom_error("An error occurred", error=e, log_stream=captured_output)
    
    output = captured_output.getvalue()
    
    assert "An error occurred" in output
    assert "Exception Type" in output
    assert "Test exception" in output

def test_log_custom_error_different_levels():
    """Test logging with different log levels"""
    # Create a StringIO to capture log output
    captured_output = StringIO()

    log_custom_error("Warning message", log_level="WARNING", log_stream=captured_output)
    output = captured_output.getvalue()
    
    assert "Warning message" in output
    assert "ERROR" in output

def test_log_custom_error_invalid_level():
    """Test that an invalid log level raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_custom_error("Test message", log_level="INVALID")

def test_log_custom_error_none_message():
    """Test logging with None message"""
    # Create a StringIO to capture log output
    captured_output = StringIO()

    log_custom_error("None error", error=None, log_stream=captured_output)
    output = captured_output.getvalue()
    
    assert "None error" in output