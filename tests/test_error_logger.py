import io
import sys
import pytest
from src.error_logger import log_error

def test_log_error_to_stderr(capsys):
    """Test that the error is logged to stderr"""
    log_error("Test error message")
    captured = capsys.readouterr()
    assert captured.err.strip() == "ERROR: Test error message"
    assert captured.out == ""

def test_log_error_with_non_string_raises_type_error():
    """Test that non-string input raises a TypeError"""
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(123)
    
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(None)

def test_log_error_with_empty_string():
    """Test logging an empty string"""
    log_error("")
    captured = capsys.readouterr()
    assert captured.err.strip() == "ERROR: "