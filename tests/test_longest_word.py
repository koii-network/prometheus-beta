import pytest
from src.longest_word import find_longest_word

def test_find_longest_word_basic():
    """Test basic functionality of finding the longest word."""
    assert find_longest_word("The quick brown fox jumps over the lazy dog") == "quick"

def test_find_longest_word_multiple_same_length():
    """Test that the first longest word is returned when multiple exist."""
    assert find_longest_word("cat dog elephant mouse") == "elephant"

def test_find_longest_word_single_word():
    """Test with a single word."""
    assert find_longest_word("hello") == "hello"

def test_find_longest_word_with_punctuation():
    """Test finding longest word with punctuation."""
    assert find_longest_word("Hello, world! Programming is fun.") == "Programming"

def test_find_longest_word_raises_on_empty_string():
    """Test that empty string raises ValueError."""
    with pytest.raises(ValueError, match="Input sentence cannot be empty"):
        find_longest_word("")
    
    with pytest.raises(ValueError, match="Input sentence cannot be empty"):
        find_longest_word("   \t\n")

def test_find_longest_word_raises_on_non_string():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(None)

def test_find_longest_word_case_sensitive():
    """Test that the function is case-sensitive."""
    assert find_longest_word("Python python PYTHON") == "PYTHON"