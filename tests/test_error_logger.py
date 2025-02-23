import pytest
import logging
import sys
from io import StringIO
from src.error_logger import log_custom_error

def test_log_custom_error_message():
    """Test basic error message logging"""
    # Redirect stderr to capture log output
    old_stderr = sys.stderr
    sys.stderr = captured_output = StringIO()

    try:
        log_custom_error("Test error message")
        output = captured_output.getvalue()
        
        assert "Test error message" in output
        assert "ERROR" in output
    finally:
        sys.stderr = old_stderr

def test_log_custom_error_with_exception():
    """Test logging with an exception"""
    # Redirect stderr to capture log output
    old_stderr = sys.stderr
    sys.stderr = captured_output = StringIO()

    try:
        try:
            raise ValueError("Test exception")
        except ValueError as e:
            log_custom_error("An error occurred", error=e)
        
        output = captured_output.getvalue()
        
        assert "An error occurred" in output
        assert "ValueError" in output
        assert "Test exception" in output
    finally:
        sys.stderr = old_stderr

def test_log_custom_error_different_levels():
    """Test logging with different log levels"""
    # Redirect stderr to capture log output
    old_stderr = sys.stderr
    sys.stderr = captured_output = StringIO()

    try:
        log_custom_error("Warning message", log_level="WARNING")
        log_custom_error("Info message", log_level="INFO")
        
        output = captured_output.getvalue()
        
        assert "WARNING" in output
        assert "INFO" in output
    finally:
        sys.stderr = old_stderr

def test_log_custom_error_invalid_level():
    """Test that an invalid log level raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_custom_error("Test message", log_level="INVALID")

def test_log_custom_error_none_message():
    """Test logging with None message"""
    # Redirect stderr to capture log output
    old_stderr = sys.stderr
    sys.stderr = captured_output = StringIO()

    try:
        log_custom_error("None error", error=None)
        output = captured_output.getvalue()
        
        assert "None error" in output
    finally:
        sys.stderr = old_stderr