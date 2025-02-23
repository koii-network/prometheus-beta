import pytest
from src.unique_word_counter import count_unique_words

def test_count_unique_words_basic():
    """Test basic unique word counting"""
    assert count_unique_words("hello world hello") == 2
    assert count_unique_words("The quick brown fox jumps over the lazy dog") == 8

def test_count_unique_words_case_insensitive():
    """Test case insensitivity"""
    assert count_unique_words("Hello HELLO hello") == 1
    assert count_unique_words("Python python PYTHON") == 1

def test_count_unique_words_with_punctuation():
    """Test handling of punctuation"""
    assert count_unique_words("Hello, world! Hello, python.") == 3
    assert count_unique_words("a, b, c, A, B, C") == 3

def test_count_unique_words_edge_cases():
    """Test edge cases"""
    assert count_unique_words("") == 0
    assert count_unique_words(None) == 0
    assert count_unique_words("   ") == 0

def test_count_unique_words_complex():
    """Test more complex scenarios"""
    text = "The the THE cat, cat CAT! jumped over the lazy dog."
    assert count_unique_words(text) == 6