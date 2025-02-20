import pytest
from src.remove_duplicate_words import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic functionality of removing duplicate words."""
    assert remove_duplicate_words("the quick brown fox jumps the quick brown fox") == "the quick brown fox jumps"

def test_remove_duplicate_words_repeated_sequence():
    """Test removing duplicates in a repeated sequence."""
    assert remove_duplicate_words("hello hello world world hello") == "hello world"

def test_remove_duplicate_words_empty_string():
    """Test behavior with an empty string."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_no_duplicates():
    """Test a string with no duplicate words."""
    assert remove_duplicate_words("one two three four") == "one two three four"

def test_remove_duplicate_words_all_duplicates():
    """Test a string with all duplicate words."""
    assert remove_duplicate_words("same same same same") == "same"

def test_remove_duplicate_words_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_words(123)
        remove_duplicate_words(None)
        remove_duplicate_words(["hello", "world"])