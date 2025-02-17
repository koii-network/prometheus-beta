import io
import sys
import pytest
from src.warning_logger import log_warning

def test_log_warning_basic(capsys):
    """Test basic warning logging functionality."""
    log_warning("Test warning message")
    captured = capsys.readouterr()
    assert captured.err.strip() == "WARNING: Test warning message"
    assert captured.out == ""

def test_log_warning_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError, match="Warning message must be a string"):
        log_warning(123)
    
    with pytest.raises(TypeError, match="Warning message must be a string"):
        log_warning(None)

def test_log_warning_empty_string(capsys):
    """Test logging an empty string."""
    log_warning("")
    captured = capsys.readouterr()
    assert captured.err.strip() == "WARNING: "