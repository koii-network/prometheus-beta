import pytest
import sys
from io import StringIO
from src.error_logger import log_error

def test_log_error_prints_to_stderr():
    # Capture stderr
    old_stderr = sys.stderr
    sys.stderr = captured_output = StringIO()
    
    try:
        # Call the log_error function
        log_error("Test error message")
        
        # Check the captured output
        captured_output.seek(0)
        error_output = captured_output.read().strip()
        
        assert error_output == "ERROR: Test error message"
    finally:
        # Restore stderr
        sys.stderr = old_stderr

def test_log_error_raises_type_error_for_non_string():
    # Test that a TypeError is raised for non-string inputs
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(123)
    
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(None)

def test_log_error_handles_empty_string():
    # Capture stderr
    old_stderr = sys.stderr
    sys.stderr = captured_output = StringIO()
    
    try:
        # Call log_error with an empty string
        log_error("")
        
        # Check the captured output
        captured_output.seek(0)
        error_output = captured_output.read().strip()
        
        assert error_output == "ERROR: "
    finally:
        # Restore stderr
        sys.stderr = old_stderr