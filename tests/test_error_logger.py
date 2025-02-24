import io
import sys
import pytest

from src.error_logger import log_error

def test_log_error_basic(capsys):
    """Test basic error logging functionality."""
    log_error("Test error message")
    captured = capsys.readouterr()
    assert captured.err.strip() == "ERROR: Test error message"

def test_log_error_empty_string(capsys):
    """Test logging an empty string."""
    log_error("")
    captured = capsys.readouterr()
    assert captured.err.strip() == "ERROR: "

def test_log_error_invalid_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(123)
    
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(None)

def test_log_error_different_messages(capsys):
    """Test logging different types of error messages."""
    test_messages = [
        "Connection failed",
        "Invalid input",
        "System error"
    ]
    
    for msg in test_messages:
        log_error(msg)
        captured = capsys.readouterr()
        assert captured.err.strip() == f"ERROR: {msg}"