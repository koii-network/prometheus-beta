import pytest
from src.remove_duplicate_words import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic removal of duplicate words"""
    input_text = "hello world hello python world"
    expected = "hello world python"
    assert remove_duplicate_words(input_text) == expected

def test_remove_duplicate_words_empty_string():
    """Test empty string input"""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_no_duplicates():
    """Test string with no duplicate words"""
    input_text = "unique words only"
    assert remove_duplicate_words(input_text) == input_text

def test_remove_duplicate_words_case_sensitive():
    """Test that word removal is case-sensitive"""
    input_text = "Hello hello HELLO world"
    expected = "Hello hello HELLO world"
    assert remove_duplicate_words(input_text) == expected

def test_remove_duplicate_words_multiple_duplicates():
    """Test string with multiple duplicate words"""
    input_text = "a b c a d b e c f"
    expected = "a b c d e f"
    assert remove_duplicate_words(input_text) == expected