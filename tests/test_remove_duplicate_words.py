import pytest
from src.remove_duplicate_words import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic functionality of removing duplicate words."""
    input_str = "the quick brown fox jumps the quick brown fox"
    expected = "the quick brown fox jumps"
    assert remove_duplicate_words(input_str) == expected

def test_remove_duplicate_words_empty_string():
    """Test with an empty string."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_no_duplicates():
    """Test with a string that has no duplicate words."""
    input_str = "hello world python programming"
    assert remove_duplicate_words(input_str) == input_str

def test_remove_duplicate_words_consecutive_duplicates():
    """Test with consecutive duplicate words."""
    input_str = "hello hello world world python python"
    expected = "hello world python"
    assert remove_duplicate_words(input_str) == expected

def test_remove_duplicate_words_case_sensitive():
    """Test that the function is case-sensitive."""
    input_str = "Hello hello HELLO world"
    expected = "Hello hello HELLO world"
    assert remove_duplicate_words(input_str) == expected

def test_remove_duplicate_words_invalid_input():
    """Test that the function raises TypeError for non-string input."""
    with pytest.raises(TypeError):
        remove_duplicate_words(123)
    with pytest.raises(TypeError):
        remove_duplicate_words(None)