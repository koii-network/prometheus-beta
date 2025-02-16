import pytest
from src.suffix_array import create_suffix_array, find_substring

def test_create_suffix_array_basic():
    """Test basic suffix array creation"""
    text = "banana"
    expected = [5, 3, 1, 0, 4, 2]  # Indices of lexicographically sorted suffixes
    assert create_suffix_array(text) == expected

def test_create_suffix_array_empty():
    """Test suffix array for empty string"""
    assert create_suffix_array("") == []

def test_create_suffix_array_single_char():
    """Test suffix array for single character"""
    text = "a"
    assert create_suffix_array(text) == [0]

def test_create_suffix_array_invalid_input():
    """Test error handling for invalid input"""
    with pytest.raises(TypeError):
        create_suffix_array(123)
    with pytest.raises(TypeError):
        create_suffix_array(None)

def test_find_substring_basic():
    """Test basic substring finding"""
    text = "banana"
    pattern = "ana"
    assert find_substring(text, pattern) == [1, 3]

def test_find_substring_multiple_occurrences():
    """Test finding multiple occurrences of a substring"""
    text = "aaaaa"
    pattern = "aa"
    assert find_substring(text, pattern) == [0, 1, 2, 3]

def test_find_substring_no_occurrences():
    """Test when substring is not found"""
    text = "banana"
    pattern = "xyz"
    assert find_substring(text, pattern) == []

def test_find_substring_empty_pattern():
    """Test error handling for empty pattern"""
    with pytest.raises(ValueError):
        find_substring("banana", "")

def test_find_substring_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_substring(123, "test")
    with pytest.raises(TypeError):
        find_substring("test", 123)
    with pytest.raises(TypeError):
        find_substring(None, None)