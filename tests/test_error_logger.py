import pytest
import sys
from io import StringIO
from src.error_logger import log_error

def test_log_error_prints_to_stderr():
    # Redirect stderr to capture the output
    stderr = sys.stderr
    sys.stderr = captured_output = StringIO()
    
    try:
        # Test logging an error message
        log_error("Test error message")
        
        # Check the captured output
        captured_output.seek(0)
        assert captured_output.read().strip() == "ERROR: Test error message"
    finally:
        # Restore stderr
        sys.stderr = stderr

def test_log_error_raises_type_error_for_non_string():
    # Test that a TypeError is raised for non-string inputs
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(123)
    
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(None)

def test_log_error_handles_empty_string():
    # Test that an empty string can be logged
    stderr = sys.stderr
    sys.stderr = captured_output = StringIO()
    
    try:
        log_error("")
        
        captured_output.seek(0)
        assert captured_output.read().strip() == "ERROR: "
    finally:
        sys.stderr = stderr