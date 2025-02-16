import pytest
from src.word_counter import count_words

def test_count_words_normal_case():
    """Test counting words in a standard sentence."""
    assert count_words("Hello world") == 2
    assert count_words("This is a test sentence") == 5

def test_count_words_empty_string():
    """Test counting words in an empty string."""
    assert count_words("") == 0

def test_count_words_whitespace_string():
    """Test counting words in a string with only whitespace."""
    assert count_words("   ") == 0
    assert count_words("\t\n ") == 0

def test_count_words_multiple_spaces():
    """Test counting words with multiple spaces between words."""
    assert count_words("Hello   world  how  are  you") == 5

def test_count_words_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        count_words(123)
    with pytest.raises(TypeError):
        count_words(None)
    with pytest.raises(TypeError):
        count_words(["hello", "world"])