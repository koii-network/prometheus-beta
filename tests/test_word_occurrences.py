import pytest
from src.word_occurrences import find_word_occurrences

def test_multiple_occurrences():
    """Test finding multiple occurrences of a word"""
    result = find_word_occurrences("the cat and the dog and the bird", "the")
    assert result == [(0, 0), (12, 3), (24, 5)]

def test_single_occurrence():
    """Test finding a single occurrence of a word"""
    result = find_word_occurrences("hello world hello", "world")
    assert result == [(6, 1)]

def test_no_occurrences():
    """Test when the target word is not in the string"""
    result = find_word_occurrences("hello world", "python")
    assert result == []

def test_case_sensitive():
    """Test that search is case-sensitive"""
    result = find_word_occurrences("Hello hello HELLO", "hello")
    assert result == [(6, 1)]

def test_empty_input_raises_error():
    """Test that empty inputs raise a ValueError"""
    with pytest.raises(ValueError):
        find_word_occurrences("", "test")
    
    with pytest.raises(ValueError):
        find_word_occurrences("test test", "")

def test_non_string_input_raises_error():
    """Test that non-string inputs raise a TypeError"""
    with pytest.raises(TypeError):
        find_word_occurrences(123, "test")
    
    with pytest.raises(TypeError):
        find_word_occurrences("test test", 123)

def test_single_word_string():
    """Test finding occurrences in a single-word string"""
    result = find_word_occurrences("hello", "hello")
    assert result == [(0, 0)]

def test_word_with_punctuation():
    """Test finding a word with potential punctuation variations"""
    result = find_word_occurrences("hello, world! hello.", "hello")
    assert result == [(0, 0), (13, 2)]