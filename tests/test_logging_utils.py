import io
import sys
import pytest
from src.logging_utils import log_warning

def test_log_warning(capsys):
    """
    Test that log_warning correctly prints a warning message to stderr.
    """
    test_message = "This is a test warning"
    log_warning(test_message)
    
    # Capture the stderr output
    captured = capsys.readouterr()
    
    # Assert that the message is printed to stderr
    assert f"WARNING: {test_message}" in captured.err
    assert captured.out == ""  # Ensure nothing is printed to stdout

def test_log_warning_with_different_messages():
    """
    Test log_warning with various types of messages.
    """
    # Redirect stderr to capture output
    old_stderr = sys.stderr
    sys.stderr = captured_output = io.StringIO()
    
    try:
        # Test with different message types
        log_warning("Simple warning")
        log_warning("Warning with numbers: 12345")
        log_warning("Warning with special characters: !@#$%^&*()")
        
        # Check the captured output
        output = captured_output.getvalue()
        assert "WARNING: Simple warning" in output
        assert "WARNING: Warning with numbers: 12345" in output
        assert "WARNING: Warning with special characters: !@#$%^&*()" in output
    finally:
        # Restore stderr
        sys.stderr = old_stderr

def test_log_warning_empty_message():
    """
    Test log_warning with an empty message.
    """
    # Redirect stderr to capture output
    old_stderr = sys.stderr
    sys.stderr = captured_output = io.StringIO()
    
    try:
        log_warning("")
        
        # Check the captured output
        output = captured_output.getvalue()
        assert "WARNING: " in output
    finally:
        # Restore stderr
        sys.stderr = old_stderr