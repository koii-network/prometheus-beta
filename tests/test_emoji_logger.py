import pytest
import logging
import io
import sys
from src.emoji_logger import emoji_log

def test_default_emoji_logging():
    """Test default emoji logging for different levels"""
    # Capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Log messages at different levels
    emoji_log("Test info message")
    emoji_log("Test warning", level='warning')
    emoji_log("Test error", level='error')
    
    # Check log output
    log_output = log_capture.getvalue()
    assert '📝 Test info message' in log_output
    assert '⚠️ Test warning' in log_output
    assert '❌ Test error' in log_output

def test_custom_emoji_logging():
    """Test custom emoji logging"""
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    emoji_log("Custom emoji message", emoji='🌟')
    
    log_output = log_capture.getvalue()
    assert '🌟 Custom emoji message' in log_output

def test_invalid_log_level():
    """Test that invalid log levels raise a ValueError"""
    with pytest.raises(ValueError, match="Invalid log level"):
        emoji_log("Invalid level test", level='invalid')

def test_all_log_levels():
    """Test logging at all supported levels"""
    log_levels = ['debug', 'info', 'warning', 'error', 'critical']
    
    for level in log_levels:
        log_capture = io.StringIO()
        logging.basicConfig(stream=log_capture, level=logging.DEBUG)
        
        emoji_log(f"Test {level} message", level=level)
        
        log_output = log_capture.getvalue()
        assert log_output, f"No output for {level} level"