import pytest
import sys
from io import StringIO
from src.error_logger import log_error

def test_log_error_valid_message():
    """Test logging a valid error message."""
    # Redirect stderr to capture output
    captured_output = StringIO()
    sys.stderr = captured_output
    
    # Log an error message
    log_error("Test error message")
    
    # Reset redirect
    sys.stderr = sys.__stderr__
    
    # Check the captured output
    assert captured_output.getvalue().strip() == "ERROR: Test error message"

def test_log_error_empty_string():
    """Test logging an empty string."""
    # Redirect stderr to capture output
    captured_output = StringIO()
    sys.stderr = captured_output
    
    # Log an empty error message
    log_error("")
    
    # Reset redirect
    sys.stderr = sys.__stderr__
    
    # Check the captured output
    assert captured_output.getvalue().strip() == "ERROR: "

def test_log_error_invalid_type():
    """Test logging with an invalid input type raises TypeError."""
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(123)
    
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(None)