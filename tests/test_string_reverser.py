import pytest
from src.string_reverser import reverse_string

def test_reverse_single_word():
    """Test reversing a single word."""
    assert reverse_string("hello") == "olleh"

def test_reverse_multi_word_string():
    """Test reversing a multi-word string."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_characters():
    """Test reversing a string with special characters."""
    assert reverse_string("hello, world!") == "!dlrow ,olleh"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_with_numbers_and_symbols():
    """Test reversing a string with numbers and symbols."""
    assert reverse_string("a1b2c3!@#") == "#@!3c2b1a"

def test_input_type_validation():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)