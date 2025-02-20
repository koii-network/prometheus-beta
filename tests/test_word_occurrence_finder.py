import pytest
from src.word_occurrence_finder import find_word_occurrences

def test_basic_occurrence():
    """Test finding a word with a single occurrence"""
    text = "hello world python hello"
    assert find_word_occurrences(text, "hello") == [(0, "hello"), (18, "hello")]

def test_no_occurrences():
    """Test when the target word is not in the string"""
    text = "hello world python"
    assert find_word_occurrences(text, "java") == []

def test_single_word_text():
    """Test with a single-word text"""
    text = "python"
    assert find_word_occurrences(text, "python") == [(0, "python")]

def test_empty_string():
    """Test with an empty string"""
    text = ""
    assert find_word_occurrences(text, "test") == []

def test_case_sensitive():
    """Test case sensitivity"""
    text = "Hello hello HELLO"
    assert find_word_occurrences(text, "hello") == [(6, "hello")]

def test_multiple_words_different_lengths():
    """Test with multiple words of different lengths"""
    text = "short longer longest short again"
    assert find_word_occurrences(text, "short") == [(0, "short"), (26, "short")]