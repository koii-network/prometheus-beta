import pytest
import sys
from io import StringIO
from src.bold_logger import log_bold

def test_log_bold_basic():
    """Test basic functionality of logging a bold message."""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Call the function
    result = log_bold("Hello, World!")
    
    # Reset redirect
    sys.stdout = sys.__stdout__
    
    # Check the output
    assert result == "\033[1mHello, World!\033[0m"
    assert captured_output.getvalue().strip() == "\033[1mHello, World!\033[0m"

def test_log_bold_empty_string():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_bold("")

def test_log_bold_whitespace_string():
    """Test that a whitespace-only string raises a ValueError."""
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_bold("   \t\n")

def test_log_bold_non_string_input():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_bold(123)
    
    with pytest.raises(TypeError, match="Message must be a string"):
        log_bold(None)

def test_log_bold_unicode():
    """Test logging a message with unicode characters."""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Call the function
    result = log_bold("こんにちは")
    
    # Reset redirect
    sys.stdout = sys.__stdout__
    
    # Check the output
    assert result == "\033[1mこんにちは\033[0m"
    assert captured_output.getvalue().strip() == "\033[1mこんにちは\033[0m"