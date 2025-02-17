import pytest
from src.bold_logger import log_bold

def test_log_bold_basic():
    """Test that log_bold wraps message with bold ANSI codes."""
    message = "Hello, World!"
    bold_message = log_bold(message)
    assert bold_message == "\033[1mHello, World!\033[0m"

def test_log_bold_empty_string():
    """Test logging an empty string."""
    message = ""
    bold_message = log_bold(message)
    assert bold_message == "\033[1m\033[0m"

def test_log_bold_special_characters():
    """Test logging message with special characters."""
    message = "!@#$%^&*()"
    bold_message = log_bold(message)
    assert bold_message == "\033[1m!@#$%^&*()\033[0m"

def test_log_bold_unicode():
    """Test logging message with unicode characters."""
    message = "こんにちは"
    bold_message = log_bold(message)
    assert bold_message == "\033[1mこんにちは\033[0m"