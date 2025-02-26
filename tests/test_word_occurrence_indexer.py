import pytest
from src.word_occurrence_indexer import find_word_occurrences

def test_basic_occurrence():
    """Test finding a word with a single occurrence"""
    result = find_word_occurrences("hello world hello", "hello")
    assert result == [(0, "hello"), (12, "hello")]

def test_no_occurrences():
    """Test when target word is not in the string"""
    result = find_word_occurrences("python is awesome", "java")
    assert result == []

def test_single_word_string():
    """Test with a single-word string"""
    result = find_word_occurrences("python", "python")
    assert result == [(0, "python")]

def test_case_sensitive():
    """Test case sensitivity of word matching"""
    result = find_word_occurrences("Hello hello HELLO", "hello")
    assert result == [(6, "hello")]

def test_multiple_words_same_target():
    """Test multiple occurrences of target word"""
    result = find_word_occurrences("cat dog cat bird cat", "cat")
    assert result == [(0, "cat"), (8, "cat"), (17, "cat")]

def test_error_non_string_input():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError, match="input_string must be a string"):
        find_word_occurrences(123, "word")
    
    with pytest.raises(TypeError, match="target_word must be a string"):
        find_word_occurrences("hello world", 123)

def test_error_empty_target_word():
    """Test error handling for empty target word"""
    with pytest.raises(ValueError, match="target_word cannot be an empty string"):
        find_word_occurrences("hello world", "")