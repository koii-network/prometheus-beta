import os
import logging
import pytest
from src.error_logger import log_error

def test_log_error_with_default_message():
    # Ensure log file is empty before test
    log_file = 'logs/error.log'
    if os.path.exists(log_file):
        os.remove(log_file)

    @log_error()
    def raise_value_error():
        raise ValueError("Test error")

    # Expect the function to raise the original exception
    with pytest.raises(ValueError, match="Test error"):
        raise_value_error()

    # Check if error was logged
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "Test error" in log_content
        assert "ValueError" in log_content

def test_log_error_with_custom_message():
    # Ensure log file is empty before test
    log_file = 'logs/error.log'
    if os.path.exists(log_file):
        os.remove(log_file)

    @log_error("Custom error message")
    def raise_type_error():
        raise TypeError("Original error")

    # Expect the function to raise the original exception
    with pytest.raises(TypeError, match="Original error"):
        raise_type_error()

    # Check if custom error message was logged
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "Custom error message" in log_content
        assert "TypeError" in log_content
        assert "Original error" in log_content

def test_log_error_no_exception():
    @log_error()
    def no_error_function():
        return "Success"

    # Ensure function works normally without an exception
    result = no_error_function()
    assert result == "Success"