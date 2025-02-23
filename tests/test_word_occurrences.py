import pytest
from src.word_occurrences import find_word_occurrences

def test_basic_occurrence():
    """Test finding a simple word occurrence"""
    result = find_word_occurrences("hello world hello", "hello")
    assert result == [(0, "hello"), (12, "hello")]

def test_no_occurrences():
    """Test when target word is not in the string"""
    result = find_word_occurrences("hello world python", "java")
    assert result == []

def test_empty_inputs():
    """Test empty string and empty target word"""
    assert find_word_occurrences("", "test") == []
    assert find_word_occurrences("test test", "") == []

def test_type_errors():
    """Test type validation"""
    with pytest.raises(TypeError):
        find_word_occurrences(123, "test")
    with pytest.raises(TypeError):
        find_word_occurrences("test", 123)

def test_single_occurrence():
    """Test string with a single occurrence"""
    result = find_word_occurrences("python is awesome", "is")
    assert result == [(7, "is")]

def test_multiple_spaces():
    """Test string with multiple spaces"""
    result = find_word_occurrences("hello   world   hello", "hello")
    assert result == [(0, "hello"), (15, "hello")]

def test_case_sensitive():
    """Test case sensitivity"""
    result = find_word_occurrences("Hello hello HELLO", "hello")
    assert result == [(6, "hello")]