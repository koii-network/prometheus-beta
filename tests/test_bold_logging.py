import pytest
from src.bold_logging import log_bold

def test_log_bold_normal_text():
    """Test logging a simple string in bold."""
    result = log_bold("Hello, World!")
    assert result == "\033[1mHello, World!\033[0m"

def test_log_bold_empty_string():
    """Test logging an empty string."""
    result = log_bold("")
    assert result == "\033[1m\033[0m"

def test_log_bold_with_special_characters():
    """Test logging a string with special characters."""
    result = log_bold("Hello, @#$%^&*()!")
    assert result == "\033[1mHello, @#$%^&*()!\033[0m"

def test_log_bold_with_numbers():
    """Test logging a string with numbers."""
    result = log_bold("123 Testing")
    assert result == "\033[1m123 Testing\033[0m"