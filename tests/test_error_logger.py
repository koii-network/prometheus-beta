import pytest
import sys
from io import StringIO
from src.error_logger import log_error

def test_log_error_outputs_to_stderr():
    # Capture stderr
    old_stderr = sys.stderr
    sys.stderr = captured_stderr = StringIO()
    
    try:
        # Call the log_error function
        log_error("Test error message")
        
        # Check the captured output
        captured_stderr.seek(0)
        output = captured_stderr.read().strip()
        assert output == "ERROR: Test error message"
    finally:
        # Restore stderr
        sys.stderr = old_stderr

def test_log_error_raises_type_error_for_non_string():
    # Test that TypeError is raised for non-string inputs
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(123)
    
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(None)
    
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(["error"])