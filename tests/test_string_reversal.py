import pytest
from src.string_reversal import reverse_string_recursive

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string_recursive("") == ""

def test_reverse_single_character():
    """Test reversing a single character string."""
    assert reverse_string_recursive("a") == "a"

def test_reverse_simple_string():
    """Test reversing a simple string."""
    assert reverse_string_recursive("hello") == "olleh"

def test_reverse_palindrome():
    """Test reversing a palindrome."""
    assert reverse_string_recursive("racecar") == "racecar"

def test_reverse_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string_recursive("hello world") == "dlrow olleh"

def test_reverse_with_special_characters():
    """Test reversing a string with special characters."""
    assert reverse_string_recursive("a1b2c3") == "3c2b1a"

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string_recursive(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string_recursive(None)