import pytest
from src.word_counter import count_words

def test_count_words_normal_sentence():
    """Test counting words in a normal sentence."""
    assert count_words("Hello world") == 2

def test_count_words_multiple_spaces():
    """Test counting words with multiple spaces between words."""
    assert count_words("Hello   world   python") == 3

def test_count_words_leading_trailing_spaces():
    """Test counting words with leading and trailing spaces."""
    assert count_words("  Hello world  ") == 2

def test_count_words_empty_string():
    """Test counting words in an empty string."""
    assert count_words("") == 0

def test_count_words_whitespace_only():
    """Test counting words in a string with only whitespaces."""
    assert count_words("    \t\n  ") == 0

def test_count_words_none_input():
    """Test handling None input."""
    assert count_words(None) == 0

def test_count_words_mixed_whitespace():
    """Test counting words with mixed whitespace characters."""
    assert count_words("Hello\tworld\n python") == 3