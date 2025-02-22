import pytest
import logging
import io
import sys
from src.emoji_logger import log_with_emoji

def test_default_log_levels():
    # Capture logging output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Test info log
    log_with_emoji("Test info message")
    assert "📝 Test info message" in log_capture.getvalue()
    log_capture.truncate(0)
    log_capture.seek(0)
    
    # Test warning log
    log_with_emoji("Test warning message", level='warning')
    assert "⚠️ Test warning message" in log_capture.getvalue()
    log_capture.truncate(0)
    log_capture.seek(0)
    
    # Test error log
    log_with_emoji("Test error message", level='error')
    assert "❌ Test error message" in log_capture.getvalue()

def test_custom_emoji():
    # Capture logging output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Test custom emoji
    log_with_emoji("Custom emoji message", emoji='🚀')
    assert "🚀 Custom emoji message" in log_capture.getvalue()

def test_invalid_log_level():
    # Test invalid log level raises ValueError
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_emoji("Invalid level test", level='invalid')

def test_log_without_emoji():
    # Capture logging output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Test logging without emoji
    log_with_emoji("No emoji message", emoji='')
    assert "No emoji message" in log_capture.getvalue()