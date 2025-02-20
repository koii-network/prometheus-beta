import pytest
from src.unique_word_counter import count_unique_words

def test_basic_unique_word_count():
    """Test counting unique words in a simple sentence"""
    text = "the quick brown fox jumps over the lazy dog"
    assert count_unique_words(text) == 8

def test_case_insensitive():
    """Test that word count is case-insensitive"""
    text = "Hello HELLO hello world World WORLD"
    assert count_unique_words(text) == 2

def test_punctuation_handling():
    """Test that punctuation is ignored"""
    text = "Hello, world! Hello, python. Python is awesome."
    assert count_unique_words(text) == 5

def test_empty_string():
    """Test handling of empty string"""
    text = ""
    assert count_unique_words(text) == 0

def test_single_word():
    """Test with a single word"""
    text = "unique"
    assert count_unique_words(text) == 1

def test_multiple_spaces_and_symbols():
    """Test with multiple spaces and symbols"""
    text = "  word1,  word2!  word1@ word3#  "
    assert count_unique_words(text) == 3