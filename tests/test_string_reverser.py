import pytest
from src.string_reverser import reverse_string_in_place

def test_reverse_string_normal():
    """Test reversing a normal string."""
    assert reverse_string_in_place("hello") == "olleh"

def test_reverse_string_empty():
    """Test reversing an empty string."""
    assert reverse_string_in_place("") == ""

def test_reverse_string_single_char():
    """Test reversing a single character string."""
    assert reverse_string_in_place("a") == "a"

def test_reverse_string_palindrome():
    """Test reversing a palindrome."""
    assert reverse_string_in_place("racecar") == "racecar"

def test_reverse_string_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string_in_place("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    """Test reversing a string with special characters."""
    assert reverse_string_in_place("a1b2c3") == "3c2b1a"

def test_reverse_string_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        reverse_string_in_place(12345)
    with pytest.raises(TypeError):
        reverse_string_in_place(None)