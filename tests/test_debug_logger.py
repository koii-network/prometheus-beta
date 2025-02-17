import os
import logging
import pytest
from src.debug_logger import conditional_debug_log

def test_debug_logger_with_env_var(caplog):
    # Test when DEBUG environment variable is set to true
    os.environ['DEBUG'] = 'true'
    caplog.set_level(logging.DEBUG)
    
    result = conditional_debug_log("Test debug message")
    assert result is True
    assert "Test debug message" in caplog.text

def test_debug_logger_with_env_var_false(caplog):
    # Test when DEBUG environment variable is set to false
    os.environ['DEBUG'] = 'false'
    caplog.set_level(logging.DEBUG)
    
    result = conditional_debug_log("Test debug message")
    assert result is False
    assert "Test debug message" not in caplog.text

def test_debug_logger_explicit_enabled(caplog):
    # Test with explicit debug_enabled=True
    os.environ['DEBUG'] = 'false'  # Ensure env var doesn't interfere
    caplog.set_level(logging.DEBUG)
    
    result = conditional_debug_log("Test debug message", debug_enabled=True)
    assert result is True
    assert "Test debug message" in caplog.text

def test_debug_logger_explicit_disabled(caplog):
    # Test with explicit debug_enabled=False
    os.environ['DEBUG'] = 'true'  # Ensure env var doesn't interfere
    caplog.set_level(logging.DEBUG)
    
    result = conditional_debug_log("Test debug message", debug_enabled=False)
    assert result is False
    assert "Test debug message" not in caplog.text