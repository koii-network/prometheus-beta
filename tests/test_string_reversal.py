import pytest
from src.string_reversal import reverse_string

def test_reverse_simple_string():
    """Test reversing a simple string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_multiple_words():
    """Test reversing multiple words."""
    assert reverse_string("hello world") == "world hello"

def test_reverse_with_special_characters():
    """Test reversing string with special characters."""
    assert reverse_string("a1b2c3!@#") == "3c2b1a!@#"

def test_reverse_with_punctuation():
    """Test reversing string with punctuation."""
    assert reverse_string("hello, world!") == "world! hello,"

def test_reverse_mixed_string():
    """Test reversing a mixed string with words and special characters."""
    assert reverse_string("h3llo w0rld!") == "w0rld h3llo!"

def test_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_single_character():
    """Test reversing a single character."""
    assert reverse_string("a") == "a"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
        reverse_string(None)