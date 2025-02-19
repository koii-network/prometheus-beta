import pytest
from src.string_reversal import reverse_string

def test_reverse_single_word():
    """Test reversing a single word."""
    assert reverse_string("hello") == "olleh"

def test_reverse_multiple_words():
    """Test reversing a multi-word string."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_characters():
    """Test reversing a string with special characters."""
    assert reverse_string("hello! world?") == "?dlrow !olleh"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_with_numbers_and_symbols():
    """Test reversing a string with numbers and symbols."""
    assert reverse_string("hello123!@#") == "#@!321olleh"

def test_reverse_type_error():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
        reverse_string(None)
        reverse_string(["hello"])