import pytest
import sys
from io import StringIO

from src.console_logger import log_message

def test_log_message_normal_case(capsys):
    """Test logging a normal message."""
    log_message("Hello, World!")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"

def test_log_message_with_spaces(capsys):
    """Test logging a message with leading and trailing spaces."""
    log_message("  Test Message  ")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Test Message"

def test_log_message_error_non_string():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(123)

def test_log_message_error_empty_string():
    """Test that a ValueError is raised for empty strings."""
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_message("")
    
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_message("   ")  # Only whitespace