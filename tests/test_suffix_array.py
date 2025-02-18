import pytest
from src.suffix_array import create_suffix_array, find_substring

def test_create_suffix_array_basic():
    """Test basic suffix array creation"""
    s = "banana"
    expected = [5, 3, 1, 0, 4, 2]  # Sorted suffix indices
    assert create_suffix_array(s) == expected

def test_create_suffix_array_empty():
    """Test suffix array for empty string"""
    assert create_suffix_array("") == []

def test_create_suffix_array_single_char():
    """Test suffix array for single character string"""
    assert create_suffix_array("a") == [0]

def test_create_suffix_array_invalid_input():
    """Test error handling for invalid input"""
    with pytest.raises(TypeError):
        create_suffix_array(123)
    with pytest.raises(TypeError):
        create_suffix_array(None)

def test_find_substring_basic():
    """Test basic substring finding"""
    s = "banana"
    assert find_substring(s, "ana") == [1, 3]
    assert find_substring(s, "an") == [1, 3]
    assert find_substring(s, "banana") == [0]

def test_find_substring_no_match():
    """Test substring that doesn't exist"""
    s = "banana"
    assert find_substring(s, "xyz") == []

def test_find_substring_edge_cases():
    """Test various edge cases for substring finding"""
    s = "banana"
    assert find_substring(s, "") == []
    assert find_substring(s, "a") == [1, 3, 5]

def test_find_substring_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_substring(123, "abc")
    with pytest.raises(TypeError):
        find_substring("abc", 123)