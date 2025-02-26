import pytest
from src.string_reversal import reverse_string

def test_reverse_string_normal():
    """Test reversing a normal string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_string_palindrome():
    """Test reversing a palindrome."""
    assert reverse_string("racecar") == "racecar"

def test_reverse_string_empty():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_single_character():
    """Test reversing a single character string."""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    """Test reversing a string with special characters."""
    assert reverse_string("a1b2c3!@#") == "#@!3c2b1a"

def test_reverse_string_numeric():
    """Test reversing a numeric string."""
    assert reverse_string("12345") == "54321"

def test_reverse_string_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        reverse_string(12345)
    with pytest.raises(TypeError):
        reverse_string(None)