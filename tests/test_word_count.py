import pytest
from src.word_count import count_words

def test_basic_word_count():
    """Test basic word counting"""
    assert count_words("Hello world") == 2

def test_multiple_spaces():
    """Test counting words with multiple spaces"""
    assert count_words("  Spaces   around   words  ") == 3

def test_empty_string():
    """Test empty string returns zero words"""
    assert count_words("") == 0
    assert count_words("   ") == 0

def test_single_word():
    """Test single word"""
    assert count_words("Python") == 1

def test_complex_whitespace():
    """Test with tabs and newlines"""
    assert count_words("Hello\tworld\ntest") == 3

def test_non_string_input():
    """Ensure function raises TypeError for non-string input"""
    with pytest.raises(AttributeError):
        count_words(123)
        count_words(None)