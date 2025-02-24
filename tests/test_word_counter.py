import pytest
from src.word_counter import count_words

def test_basic_word_counting():
    """Test basic word counting scenarios."""
    assert count_words("Hello world") == 2
    assert count_words("This is a test sentence") == 5

def test_multiple_whitespaces():
    """Test word counting with multiple and varied whitespaces."""
    assert count_words("   Hello   world   ") == 2
    assert count_words("\tHello\t\tworld\n") == 2

def test_empty_and_whitespace_strings():
    """Test edge cases with empty and whitespace-only strings."""
    assert count_words("") == 0
    assert count_words("   ") == 0
    assert count_words("\t\n\r") == 0

def test_single_word():
    """Test counting words in single-word strings."""
    assert count_words("Python") == 1

def test_none_and_non_string_inputs():
    """Test handling of None and non-string inputs."""
    assert count_words(None) == 0
    assert count_words(42) == 1
    assert count_words(["hello", "world"]) == 1  # converts to string representation

def test_special_characters():
    """Test word counting with special characters."""
    assert count_words("Hello, world!") == 2
    assert count_words("Python-programming") == 1