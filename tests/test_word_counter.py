import pytest
from src.word_counter import count_words

def test_basic_word_counting():
    """Test basic word counting functionality."""
    assert count_words("hello world") == 2
    assert count_words("  hello   world  ") == 2

def test_single_word():
    """Test counting single word."""
    assert count_words("hello") == 1

def test_empty_string():
    """Test empty string returns zero words."""
    assert count_words("") == 0
    assert count_words("   ") == 0

def test_multiple_spaces():
    """Test multiple spaces between words."""
    assert count_words("hello    world") == 2

def test_tabs_and_newlines():
    """Test counting words with tabs and newlines."""
    assert count_words("hello\tworld\ntest") == 3

def test_invalid_input():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        count_words(123)
    
    with pytest.raises(TypeError):
        count_words(None)

def test_complex_whitespace():
    """Test complex whitespace scenarios."""
    assert count_words("\n\t hello \t world \n test \t") == 3