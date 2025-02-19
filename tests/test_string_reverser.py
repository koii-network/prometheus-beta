import pytest
from src.string_reverser import reverse_string

def test_reverse_single_word():
    """Test reversing a simple single word."""
    assert reverse_string("hello") == "olleh"

def test_reverse_multi_word():
    """Test reversing a multi-word string."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_with_special_characters():
    """Test reversing a string with special characters."""
    assert reverse_string("Hello, World! 123") == "321 !dlroW ,olleH"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_with_spaces():
    """Test reversing a string with multiple spaces."""
    assert reverse_string("  spaced  ") == "  decaps  "

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
        reverse_string(None)
        reverse_string(["hello"])