import pytest
from src.bold_logger import log_bold

def test_log_bold_basic():
    """Test basic bold logging functionality."""
    message = "Hello, World!"
    bold_message = log_bold(message)
    assert bold_message == "\033[1mHello, World!\033[0m"

def test_log_bold_empty_string():
    """Test logging an empty string."""
    message = ""
    bold_message = log_bold(message)
    assert bold_message == "\033[1m\033[0m"

def test_log_bold_with_special_characters():
    """Test logging a message with special characters."""
    message = "Test@#$%^&*()"
    bold_message = log_bold(message)
    assert bold_message == "\033[1mTest@#$%^&*()\033[0m"

def test_log_bold_type():
    """Test that the function returns a string."""
    message = "Test Message"
    bold_message = log_bold(message)
    assert isinstance(bold_message, str)