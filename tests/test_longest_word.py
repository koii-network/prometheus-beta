import pytest
from src.longest_word import find_longest_word

def test_find_longest_word_basic():
    """Test finding the longest word in a normal sentence."""
    assert find_longest_word("The quick brown fox jumps") == "quick"

def test_find_longest_word_multiple_max_length():
    """Test that the first longest word is returned when multiple words have same length."""
    assert find_longest_word("cat dog elephant") == "elephant"

def test_find_longest_word_empty_string():
    """Test behavior with an empty string."""
    assert find_longest_word("") == ""

def test_find_longest_word_whitespace_only():
    """Test behavior with string containing only whitespace."""
    assert find_longest_word("   \t\n  ") == ""

def test_find_longest_word_with_punctuation():
    """Test finding longest word with punctuation."""
    assert find_longest_word("Hello, world! Python-programming") == "Python-programming"

def test_find_longest_word_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(None)

def test_find_longest_word_single_word():
    """Test finding longest word with a single word."""
    assert find_longest_word("hello") == "hello"