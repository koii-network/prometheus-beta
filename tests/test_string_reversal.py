import pytest
from src.string_reversal import recursive_reverse_string

def test_empty_string():
    """Test reversing an empty string."""
    assert recursive_reverse_string("") == ""

def test_single_character():
    """Test reversing a single character string."""
    assert recursive_reverse_string("a") == "a"

def test_multiple_characters():
    """Test reversing a string with multiple characters."""
    assert recursive_reverse_string("hello") == "olleh"

def test_palindrome():
    """Test a palindrome string remains the same."""
    assert recursive_reverse_string("racecar") == "racecar"

def test_with_spaces():
    """Test reversing a string with spaces."""
    assert recursive_reverse_string("hello world") == "dlrow olleh"

def test_with_special_characters():
    """Test reversing a string with special characters."""
    assert recursive_reverse_string("h3llo!") == "!3olleh"