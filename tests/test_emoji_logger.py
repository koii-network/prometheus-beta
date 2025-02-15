import pytest
import logging
import emoji
from src.emoji_logger import log_with_emoji

def test_log_with_default_level(caplog):
    caplog.set_level(logging.INFO)
    result = log_with_emoji("Test message")
    assert "Test message" in caplog.text
    assert result == "Test message"

def test_log_with_emoji(caplog):
    caplog.set_level(logging.INFO)
    result = log_with_emoji("Hello", emoji_symbol="smile")
    assert emoji.is_emoji(result.split()[0]) 
    assert "Hello" in result

def test_log_with_unicode_emoji(caplog):
    caplog.set_level(logging.INFO)
    result = log_with_emoji("Greeting", emoji_symbol="😊")
    assert emoji.is_emoji(result.split()[0])
    assert "Greeting" in result

def test_log_different_levels(caplog):
    caplog.set_level(logging.ERROR)
    
    result_warning = log_with_emoji("Warning message", level="warning", emoji_symbol="warning")
    result_error = log_with_emoji("Error message", level="error", emoji_symbol="x")
    
    assert "Warning message" in caplog.text
    assert "Error message" in caplog.text

def test_invalid_logging_level():
    with pytest.raises(ValueError, match="Invalid logging level"):
        log_with_emoji("Test", level="invalid")

def test_fallback_on_invalid_emoji(caplog):
    caplog.set_level(logging.INFO)
    result = log_with_emoji("Fallback message", emoji_symbol="not_a_real_emoji")
    assert result == "Fallback message"