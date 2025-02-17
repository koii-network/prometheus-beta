import logging
import pytest
from src.multi_logger import log_multiple_values

def test_log_multiple_string_values(caplog):
    """Test logging multiple string values"""
    caplog.set_level(logging.INFO)
    log_multiple_values("Hello", "World", "Test")
    assert "Hello World Test" in caplog.text

def test_log_multiple_mixed_values(caplog):
    """Test logging multiple mixed type values"""
    caplog.set_level(logging.INFO)
    log_multiple_values("Number:", 42, "Boolean:", True)
    assert "Number: 42 Boolean: True" in caplog.text

def test_log_with_custom_level(caplog):
    """Test logging with a custom log level"""
    caplog.set_level(logging.WARNING)
    log_multiple_values("Warning", "message", level=logging.WARNING)
    assert "Warning message" in caplog.text

def test_log_with_custom_logger(caplog):
    """Test logging with a custom logger"""
    custom_logger = logging.getLogger('custom_logger')
    caplog.set_level(logging.INFO, logger=custom_logger)
    log_multiple_values("Custom", "Logger", "Test", logger=custom_logger)
    assert "Custom Logger Test" in caplog.text

def test_log_no_values(caplog):
    """Test logging with no values"""
    caplog.set_level(logging.INFO)
    log_multiple_values()
    assert "" in caplog.text  # No log message is fine