import pytest
from src.string_utils import remove_char_length

def test_remove_char_length_basic():
    """Test basic functionality of removing a character and counting length."""
    assert remove_char_length("hello", "l") == 3
    assert remove_char_length("python", "o") == 5
    assert remove_char_length("mississippi", "s") == 7

def test_remove_char_length_no_match():
    """Test when the character is not in the string."""
    assert remove_char_length("hello", "x") == 5
    assert remove_char_length("", "a") == 0

def test_remove_char_length_empty_string():
    """Test with an empty string."""
    assert remove_char_length("", "a") == 0

def test_remove_char_length_multiple_removals():
    """Test removing multiple instances of a character."""
    assert remove_char_length("banana", "a") == 3
    assert remove_char_length("hello world", " ") == 10

def test_remove_char_length_invalid_inputs():
    """Test error handling for invalid input types."""
    # Test non-string inputs
    with pytest.raises(TypeError, match="Input 'string' must be a string"):
        remove_char_length(123, "a")
    
    with pytest.raises(TypeError, match="Input 'char' must be a string"):
        remove_char_length("hello", 42)

def test_remove_char_length_invalid_char():
    """Test error handling for multi-character inputs."""
    with pytest.raises(ValueError, match="Input 'char' must be a single character"):
        remove_char_length("hello", "ab")
    
    with pytest.raises(ValueError, match="Input 'char' must be a single character"):
        remove_char_length("hello", "")