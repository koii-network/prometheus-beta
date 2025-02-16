import pytest
from src.suffix_array import create_suffix_array, find_substring

def test_create_suffix_array_basic():
    """Test basic suffix array creation"""
    s = "banana"
    expected = [5, 3, 1, 0, 4, 2]  # Indices of lexicographically sorted suffixes
    assert create_suffix_array(s) == expected

def test_create_suffix_array_empty():
    """Test suffix array for empty string"""
    assert create_suffix_array("") == []

def test_create_suffix_array_single_char():
    """Test suffix array for single character string"""
    assert create_suffix_array("a") == [0]

def test_create_suffix_array_invalid_input():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError):
        create_suffix_array(123)
    with pytest.raises(TypeError):
        create_suffix_array(None)

def test_find_substring_basic():
    """Test basic substring finding"""
    s = "banana"
    pattern = "ana"
    assert find_substring(s, pattern) == [1, 3]

def test_find_substring_multiple_occurrences():
    """Test finding multiple occurrences of a substring"""
    s = "anananas"
    pattern = "ana"
    assert find_substring(s, pattern) == [0, 2, 4]

def test_find_substring_no_match():
    """Test substring that doesn't exist"""
    s = "banana"
    pattern = "xyz"
    assert find_substring(s, pattern) == []

def test_find_substring_full_string():
    """Test finding the full string"""
    s = "banana"
    pattern = "banana"
    assert find_substring(s, pattern) == [0]

def test_find_substring_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_substring(123, "pattern")
    with pytest.raises(TypeError):
        find_substring("text", 123)
    
    with pytest.raises(ValueError):
        find_substring("text", "")