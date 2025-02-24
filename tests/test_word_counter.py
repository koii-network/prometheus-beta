import pytest
from src.word_counter import count_words

def test_basic_word_counting():
    """Test basic word counting functionality."""
    assert count_words("Hello world") == 2
    assert count_words("One") == 1
    assert count_words("") == 0

def test_multiple_spaces():
    """Test handling of multiple spaces between words."""
    assert count_words("  Multiple   spaces   between words  ") == 3
    assert count_words("   Leading and trailing spaces   ") == 4

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_words(123)
    with pytest.raises(TypeError):
        count_words(None)

def test_special_cases():
    """Test various special case inputs."""
    assert count_words(" ") == 0
    assert count_words("\t\n") == 0
    assert count_words("Hello\tworld\ntest") == 3