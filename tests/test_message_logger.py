"""
Test suite for multi-line message logging utility.
"""

import pytest
from src.message_logger import log_multiline_message

def test_single_line_message():
    """Test logging a single line message."""
    result = log_multiline_message("Hello, world!")
    expected_lines = [
        '-' * 40,
        "Hello, world!",
        '-' * 40
    ]
    assert result == '\n'.join(expected_lines)

def test_multi_line_message():
    """Test logging multiple message lines."""
    messages = ["Line 1", "Line 2", "Line 3"]
    result = log_multiline_message(messages)
    expected_lines = [
        '-' * 40,
        "Line 1",
        "Line 2", 
        "Line 3",
        '-' * 40
    ]
    assert result == '\n'.join(expected_lines)

def test_custom_separator():
    """Test using a custom separator character."""
    result = log_multiline_message("Test", separator_char='*', separator_length=10)
    expected_lines = [
        '*' * 10,
        "Test",
        '*' * 10
    ]
    assert result == '\n'.join(expected_lines)

def test_invalid_separator_char():
    """Test that invalid separator raises ValueError."""
    with pytest.raises(ValueError, match="Separator must be a single character"):
        log_multiline_message("Test", separator_char='too long')

def test_invalid_message_type():
    """Test that invalid message type raises TypeError."""
    with pytest.raises(TypeError, match="Message must be a string or list of strings"):
        log_multiline_message(123)

def test_list_with_non_string():
    """Test that a list with non-string elements raises TypeError."""
    with pytest.raises(TypeError, match="Message must be a string or list of strings"):
        log_multiline_message(["Valid", 123, "Invalid"])

def test_empty_message():
    """Test logging an empty message or empty list."""
    # Empty string
    result_str = log_multiline_message("")
    expected_str = ['-' * 40, "", '-' * 40]
    assert result_str == '\n'.join(expected_str)

    # Empty list
    result_list = log_multiline_message([])
    expected_list = ['-' * 40, '-' * 40]
    assert result_list == '\n'.join(expected_list)