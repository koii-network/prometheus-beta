import pytest
from src.string_reversal import recursive_reverse_string

def test_empty_string():
    """Test reversing an empty string."""
    assert recursive_reverse_string("") == ""

def test_single_character():
    """Test reversing a single character."""
    assert recursive_reverse_string("a") == "a"

def test_simple_string():
    """Test reversing a simple lowercase string."""
    assert recursive_reverse_string("hello") == "olleh"

def test_mixed_case_string():
    """Test reversing a string with mixed case."""
    assert recursive_reverse_string("HeLLo") == "oLLeH"

def test_string_with_spaces():
    """Test reversing a string with spaces."""
    assert recursive_reverse_string("hello world") == "dlrow olleh"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse_string(123)
        recursive_reverse_string(None)
        recursive_reverse_string(["hello"])

def test_long_string():
    """Test reversing a longer string."""
    assert recursive_reverse_string("abcdefghijklmnop") == "ponmlkjihgfedcba"