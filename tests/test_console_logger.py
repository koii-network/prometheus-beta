import pytest
import sys
from io import StringIO

from src.console_logger import log_message

def test_log_message_basic():
    """Test basic message logging."""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Log a message
    log_message("Hello, World!")
    
    # Reset redirect
    sys.stdout = sys.__stdout__
    
    # Check the output
    assert captured_output.getvalue().strip() == "Hello, World!"

def test_log_message_empty_string():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_message("")
    
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_message("   ")

def test_log_message_non_string():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(123)
    
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(None)
    
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(["not", "a", "string"])