import pytest
from src.longest_word import find_longest_word

def test_find_longest_word_basic():
    """Test finding the longest word in a simple sentence."""
    assert find_longest_word("The quick brown fox jumps") == "quick"

def test_find_longest_word_multiple_same_length():
    """Test when multiple words, return the first lexicographically."""
    assert find_longest_word("cat dog bird") == "bird"

def test_find_longest_word_empty_string():
    """Test with an empty string."""
    assert find_longest_word("") == ""

def test_find_longest_word_single_word():
    """Test with a single word."""
    assert find_longest_word("hello") == "hello"

def test_find_longest_word_with_punctuation():
    """Test with words containing punctuation."""
    assert find_longest_word("Hello, world! How are you?") == "Hello"

def test_find_longest_word_with_numbers():
    """Test with words containing numbers."""
    assert find_longest_word("The year is 2023") == "year"

def test_find_longest_word_error_non_string():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        find_longest_word(123)
    with pytest.raises(TypeError):
        find_longest_word(["hello", "world"])

def test_find_longest_word_multiple_whitespaces():
    """Test with multiple whitespaces between words."""
    assert find_longest_word("   hello    world   ") == "hello"