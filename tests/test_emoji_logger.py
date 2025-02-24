import pytest
import logging
import io
import sys
from src.emoji_logger import log_with_emoji

def test_log_with_default_emoji(capfd):
    # Log a message
    log_with_emoji("Test message", emoji_symbol=":smile:")

    # Capture output
    out, err = capfd.readouterr()

    # Check output
    assert "😄 Test message" in out

def test_log_different_levels(capfd):
    # Test different log levels
    log_levels = ['debug', 'info', 'warning', 'error', 'critical']
    
    for level in log_levels:
        # Log a message
        log_with_emoji(f"Test {level} message", log_level=level)

        # Capture output
        out, err = capfd.readouterr()

        # Check output
        assert f"Test {level} message" in out

def test_invalid_log_level():
    # Test invalid log level
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_emoji("Test message", log_level="invalid")

def test_invalid_message_type():
    # Test invalid message type
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_emoji(123)

def test_log_with_custom_emoji(capfd):
    # Log a message with a custom emoji
    log_with_emoji("Custom emoji test", emoji_symbol="🚀")

    # Capture output
    out, err = capfd.readouterr()

    # Check output
    assert "🚀 Custom emoji test" in out

def test_log_without_emoji(capfd):
    # Log a message without emoji
    log_with_emoji("No emoji test")

    # Capture output
    out, err = capfd.readouterr()

    # Check output
    assert "No emoji test" in out