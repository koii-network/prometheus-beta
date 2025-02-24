import pytest
import logging
import io
import sys
from src.emoji_logger import log_with_emoji

def test_log_with_default_emoji():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Log a message
    log_with_emoji("Test message", emoji_symbol=":smile:")

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check output
    output = captured_output.getvalue().strip()
    assert "😄 Test message" in output

def test_log_different_levels():
    # Test different log levels
    log_levels = ['debug', 'info', 'warning', 'error', 'critical']
    
    for level in log_levels:
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Log a message
        log_with_emoji(f"Test {level} message", log_level=level)

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check output
        output = captured_output.getvalue().strip()
        assert f"Test {level} message" in output

def test_invalid_log_level():
    # Test invalid log level
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_emoji("Test message", log_level="invalid")

def test_invalid_message_type():
    # Test invalid message type
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_emoji(123)

def test_log_with_custom_emoji():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Log a message with a custom emoji
    log_with_emoji("Custom emoji test", emoji_symbol="🚀")

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check output
    output = captured_output.getvalue().strip()
    assert "🚀 Custom emoji test" in output

def test_log_without_emoji():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Log a message without emoji
    log_with_emoji("No emoji test")

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check output
    output = captured_output.getvalue().strip()
    assert "No emoji test" in output