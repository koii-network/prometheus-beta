import pytest
from src.unique_word_counter import count_unique_words

def test_basic_unique_word_count():
    """Test counting unique words in a simple sentence."""
    assert count_unique_words("Hello, hello! How are you?") == 4

def test_empty_string():
    """Test that an empty string returns 0 unique words."""
    assert count_unique_words("") == 0

def test_whitespace_only():
    """Test that a string with only whitespace returns 0 unique words."""
    assert count_unique_words("   ") == 0

def test_case_insensitive():
    """Test that word counting is case-insensitive."""
    assert count_unique_words("Hello HELLO hello") == 1

def test_punctuation_handling():
    """Test that punctuation is ignored when counting unique words."""
    assert count_unique_words("Hello, hello! World, world.") == 2

def test_complex_text():
    """Test counting unique words in a more complex text."""
    text = "The quick brown fox jumps over the lazy dog. The dog barks!"
    assert count_unique_words(text) == 8

def test_special_characters():
    """Test handling of special characters and mixed punctuation."""
    text = "Hello! @#$% world, hello... world?"
    assert count_unique_words(text) == 2