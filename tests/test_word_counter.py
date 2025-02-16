import pytest
from src.word_counter import count_words

def test_basic_word_counting():
    """Test basic word counting functionality."""
    assert count_words("Hello world") == 2
    assert count_words("This is a test sentence") == 5

def test_empty_string():
    """Test that an empty string returns 0 words."""
    assert count_words("") == 0
    assert count_words("   ") == 0

def test_multiple_spaces():
    """Test handling of multiple consecutive spaces."""
    assert count_words("Hello   world  test") == 3

def test_leading_trailing_spaces():
    """Test stripping of leading and trailing spaces."""
    assert count_words("  Hello world  ") == 2

def test_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_words(None)
    
    # This will check if non-string types raise TypeError
    with pytest.raises(TypeError):
        count_words(42)

def test_mixed_whitespace():
    """Test handling of mixed whitespace characters."""
    assert count_words("Hello\tworld\ntest") == 3