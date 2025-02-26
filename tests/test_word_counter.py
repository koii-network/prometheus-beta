import pytest
from src.word_counter import count_unique_words

def test_basic_unique_words():
    """Test basic unique word counting"""
    assert count_unique_words("Hello, hello! How are you?") == 4

def test_empty_string():
    """Test empty string returns 0"""
    assert count_unique_words("") == 0

def test_none_input():
    """Test None input returns 0"""
    assert count_unique_words(None) == 0

def test_case_insensitive():
    """Test case-insensitive word counting"""
    assert count_unique_words("a A a B b") == 2

def test_punctuation_handling():
    """Test punctuation is ignored"""
    assert count_unique_words("Hello! hello, world. World?") == 2

def test_complex_text():
    """Test a more complex text with multiple words"""
    text = "The quick brown fox jumps over the lazy dog. The dog barks!"
    assert count_unique_words(text) == 8

def test_whitespace_handling():
    """Test various whitespace scenarios"""
    assert count_unique_words("  word   Word  WORD  ") == 1