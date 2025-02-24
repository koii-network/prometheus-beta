import pytest
from src.unique_word_counter import count_unique_words

def test_basic_unique_word_count():
    """Test basic unique word counting"""
    assert count_unique_words("Hello, hello world! World.") == 2

def test_empty_string():
    """Test empty string returns 0"""
    assert count_unique_words("") == 0

def test_whitespace_string():
    """Test string with only whitespace returns 0"""
    assert count_unique_words("   \t\n ") == 0

def test_punctuation_handling():
    """Test that punctuation is ignored"""
    assert count_unique_words("Hello! hello, world. World;") == 2

def test_mixed_case():
    """Test that case is ignored"""
    assert count_unique_words("Hello HELLO hello") == 1

def test_complex_text():
    """Test a more complex text with multiple unique words"""
    text = "The quick brown fox jumps over the lazy dog. The quick brown fox again."
    assert count_unique_words(text) == 9

def test_none_input():
    """Test handling of None input"""
    assert count_unique_words(None) == 0