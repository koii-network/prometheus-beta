import pytest
import logging
import io
import sys
from src.log_warning import log_warning

def test_log_warning_basic():
    """Test that a warning message is logged correctly."""
    # Capture stderr
    captured_output = io.StringIO()
    sys.stderr = captured_output

    # Log a test warning
    test_message = "This is a test warning"
    log_warning(test_message)

    # Reset redirect
    sys.stderr = sys.__stderr__

    # Check if the message was logged
    logged_output = captured_output.getvalue().strip()
    assert f"WARNING: {test_message}" in logged_output

def test_log_warning_empty_string():
    """Test logging an empty warning message."""
    # Capture stderr
    captured_output = io.StringIO()
    sys.stderr = captured_output

    # Log an empty warning
    log_warning("")

    # Reset redirect
    sys.stderr = sys.__stderr__

    # Check if the message was logged
    logged_output = captured_output.getvalue().strip()
    assert "WARNING:" in logged_output

def test_log_warning_non_string_input():
    """Test logging a non-string warning message."""
    # Capture stderr
    captured_output = io.StringIO()
    sys.stderr = captured_output

    # Log a non-string warning
    test_object = {"key": "value"}
    log_warning(test_object)

    # Reset redirect
    sys.stderr = sys.__stderr__

    # Check if the message was logged
    logged_output = captured_output.getvalue().strip()
    assert "WARNING:" in logged_output
    assert str(test_object) in logged_output