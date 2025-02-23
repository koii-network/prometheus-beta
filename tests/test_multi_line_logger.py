"""
Tests for the multi-line logging function.
"""

import pytest
from src.multi_line_logger import log_multiline
import io
import sys

def test_default_logging():
    """Test default logging behavior."""
    # Redirect stdout to capture print output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Call the function
    log_multiline("Test message")
    
    # Reset redirect
    sys.stdout = sys.__stdout__
    
    # Check output
    output = captured_output.getvalue().strip().split('\n')
    assert len(output) == 3
    assert output[0] == output[2] == '=' * 40
    assert output[1] == "Test message"

def test_custom_separator():
    """Test logging with a custom separator."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    log_multiline("Test message", separator='-')
    
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip().split('\n')
    assert len(output) == 3
    assert output[0] == output[2] == '-' * 40
    assert output[1] == "Test message"

def test_custom_line_length():
    """Test logging with a custom line length."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    log_multiline("Test message", line_length=20)
    
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip().split('\n')
    assert len(output) == 3
    assert output[0] == output[2] == '=' * 20
    assert output[1] == "Test message"

def test_custom_logger():
    """Test logging with a custom logger function."""
    logger_calls = []
    def mock_logger(msg):
        logger_calls.append(msg)
    
    log_multiline("Test message", logger=mock_logger)
    
    assert len(logger_calls) == 3
    assert logger_calls[0] == '=' * 40
    assert logger_calls[1] == "Test message"
    assert logger_calls[2] == '=' * 40

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Non-string message
    with pytest.raises(TypeError, match="Message must be a string"):
        log_multiline(123)
    
    # Empty separator
    with pytest.raises(ValueError, match="Separator cannot be an empty string"):
        log_multiline("Test", separator='')
    
    # Invalid line length
    with pytest.raises(TypeError, match="Line length must be a positive integer"):
        log_multiline("Test", line_length=0)
    
    with pytest.raises(TypeError, match="Line length must be a positive integer"):
        log_multiline("Test", line_length=-5)

def test_multiline_message():
    """Test logging a multi-line message."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    log_multiline("Line 1\nLine 2\nLine 3")
    
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip().split('\n')
    assert len(output) == 5
    assert output[0] == output[4] == '=' * 40
    assert output[1] == "Line 1"
    assert output[2] == "Line 2"
    assert output[3] == "Line 3"