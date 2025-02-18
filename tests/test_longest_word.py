import pytest
from src.longest_word import find_longest_word

def test_find_longest_word_basic():
    """Test finding the longest word in a simple sentence."""
    assert find_longest_word("The quick brown fox") == "quick"

def test_find_longest_word_multiple_same_length():
    """Test that the first longest word is returned when multiple exist."""
    assert find_longest_word("red green yellow blue") == "yellow"

def test_find_longest_word_with_punctuation():
    """Test finding longest word when punctuation is present."""
    assert find_longest_word("Hello, world! Programming is fun.") == "Programming"

def test_find_longest_word_single_word():
    """Test with a single word."""
    assert find_longest_word("hello") == "hello"

def test_find_longest_word_raises_on_empty_string():
    """Test that ValueError is raised for empty string."""
    with pytest.raises(ValueError, match="Sentence cannot be empty"):
        find_longest_word("")
    with pytest.raises(ValueError, match="Sentence cannot be empty"):
        find_longest_word("   ")

def test_find_longest_word_raises_on_non_string():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(["hello", "world"])