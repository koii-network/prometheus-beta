import pytest
import sys
import io

from src.bold_logger import log_bold

def test_log_bold_basic():
    """Test basic bold logging functionality."""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Call the function
    result = log_bold("Hello, World!")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check the output and return value
    assert result == "\033[1mHello, World!\033[0m"
    assert captured_output.getvalue().strip() == "\033[1mHello, World!\033[0m"

def test_log_bold_empty_string():
    """Test that empty strings raise a ValueError."""
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_bold("")
    
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_bold("   ")

def test_log_bold_invalid_type():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(["not", "a", "string"])

def test_log_bold_different_messages():
    """Test logging various types of messages."""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Test with different message types
    messages = [
        "Simple message",
        "Message with numbers 123",
        "Message with special characters !@#$%^&*()",
        "多语言消息"  # Unicode/non-English message
    ]
    
    for msg in messages:
        result = log_bold(msg)
        assert result == f"\033[1m{msg}\033[0m"
    
    # Restore stdout
    sys.stdout = sys.__stdout__