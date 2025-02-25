import pytest
from src.remove_duplicate_words import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic functionality of removing duplicate words."""
    assert remove_duplicate_words("hello world hello python world") == "hello world python"

def test_remove_duplicate_words_with_extra_whitespace():
    """Test handling of extra whitespace."""
    assert remove_duplicate_words("  a b c a b c  ") == "a b c"

def test_remove_duplicate_words_no_duplicates():
    """Test string with no duplicate words."""
    assert remove_duplicate_words("one two three") == "one two three"

def test_remove_duplicate_words_completely_duplicated():
    """Test string that is completely duplicated."""
    assert remove_duplicate_words("a a a a") == "a"

def test_remove_duplicate_words_empty_string():
    """Test empty string input."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_words(123)
        remove_duplicate_words(None)
        remove_duplicate_words(["hello", "world"])