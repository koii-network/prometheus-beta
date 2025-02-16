import pytest
from src.word_counter import count_words

def test_count_words_normal_sentence():
    """Test counting words in a normal sentence."""
    assert count_words("Hello world") == 2

def test_count_words_multiple_spaces():
    """Test counting words with multiple spaces between words."""
    assert count_words("Hello   world   how   are   you") == 5

def test_count_words_leading_trailing_spaces():
    """Test counting words with leading and trailing spaces."""
    assert count_words("  Hello world  ") == 2

def test_count_words_empty_string():
    """Test counting words in an empty string."""
    assert count_words("") == 0

def test_count_words_only_whitespace():
    """Test counting words in a string with only whitespace."""
    assert count_words("   \t\n  ") == 0

def test_count_words_non_string_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_words(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        count_words(None)