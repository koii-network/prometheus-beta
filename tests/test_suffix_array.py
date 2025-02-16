import pytest
from src.suffix_array import create_suffix_array, find_substring

def test_create_suffix_array_basic():
    """Test basic suffix array creation"""
    text = "banana"
    expected = [5, 3, 1, 0, 4, 2]  # Indices of lexicographically sorted suffixes
    assert create_suffix_array(text) == expected

def test_create_suffix_array_empty():
    """Test suffix array with empty string"""
    assert create_suffix_array("") == []

def test_create_suffix_array_single_char():
    """Test suffix array with single character"""
    text = "a"
    assert create_suffix_array(text) == [0]

def test_create_suffix_array_invalid_input():
    """Test suffix array with invalid input types"""
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
    text = "mississippi"
    pattern = "issi"
    assert find_substring(text, pattern) == [1, 4]

def test_find_substring_no_occurrences():
    """Test when substring is not found"""
    text = "hello world"
    pattern = "python"
    assert find_substring(text, pattern) == []

def test_find_substring_edge_cases():
    """Test various edge cases for substring finding"""
    # Single character pattern
    assert find_substring("hello", "l") == [2, 3]
    
    # Entire string as pattern
    assert find_substring("hello", "hello") == [0]

def test_find_substring_invalid_inputs():
    """Test invalid inputs for substring finding"""
    with pytest.raises(TypeError):
        find_substring(123, "pattern")
    with pytest.raises(TypeError):
        find_substring("text", 123)
    
    with pytest.raises(ValueError):
        find_substring("text", "")