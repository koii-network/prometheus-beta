import pytest
from src.longest_word import find_longest_word

def test_find_longest_word_basic():
    """Test finding the longest word in a simple sentence."""
    assert find_longest_word("The quick brown fox jumps") == "quick"

def test_find_longest_word_multiple_max_length():
    """Test when multiple words have the same maximum length."""
    assert find_longest_word("cat dog mouse house") == "mouse"

def test_find_longest_word_single_word():
    """Test with a single word."""
    assert find_longest_word("hello") == "hello"

def test_find_longest_word_with_punctuation():
    """Test with words containing punctuation."""
    assert find_longest_word("Hello world! Programming is fun.") == "Programming"

def test_find_longest_word_whitespace():
    """Test with extra whitespace."""
    assert find_longest_word("  hello   world  ") == "hello"

def test_find_longest_word_invalid_input_none():
    """Test raising TypeError for None input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(None)

def test_find_longest_word_invalid_input_number():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(123)

def test_find_longest_word_empty_string():
    """Test raising ValueError for empty string."""
    with pytest.raises(ValueError, match="Input sentence cannot be empty"):
        find_longest_word("")

def test_find_longest_word_only_whitespace():
    """Test raising ValueError for whitespace-only string."""
    with pytest.raises(ValueError, match="Input sentence cannot be empty"):
        find_longest_word("   \t\n  ")