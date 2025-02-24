"""
Tests for the multi-line logging utility.
"""

import pytest
from src.multi_line_logger import log_multiline

def test_default_logging():
    """Test default logging behavior."""
    message = "Hello\nWorld"
    result = log_multiline(message)
    
    # Split the result into lines
    lines = result.split('\n')
    
    # Check total number of lines including separators
    assert len(lines) == 3
    
    # Check separator lines
    assert lines[0] == '==' * 25
    assert lines[2] == '==' * 25
    
    # Check message content
    assert lines[1] == message

def test_custom_separator():
    """Test logging with a custom separator."""
    message = "Custom Separator"
    result = log_multiline(message, separator='*', line_length=10)
    
    lines = result.split('\n')
    
    assert lines[0] == '*' * 10
    assert lines[1] == message
    assert lines[2] == '*' * 10

def test_invalid_message_type():
    """Test that non-string messages raise a TypeError."""
    with pytest.raises(TypeError):
        log_multiline(123)

def test_empty_separator():
    """Test that an empty separator raises a ValueError."""
    with pytest.raises(ValueError):
        log_multiline("Test", separator='')

def test_invalid_line_length():
    """Test that invalid line lengths raise a ValueError."""
    with pytest.raises(ValueError):
        log_multiline("Test", line_length=0)

def test_single_line_message():
    """Test logging a single-line message."""
    message = "Single Line"
    result = log_multiline(message)
    
    lines = result.split('\n')
    
    assert len(lines) == 3
    assert lines[1] == message

def test_multiline_message():
    """Test logging a multi-line message."""
    message = "Line 1\nLine 2\nLine 3"
    result = log_multiline(message)
    
    lines = result.split('\n')
    
    assert len(lines) == 3
    assert lines[1] == message