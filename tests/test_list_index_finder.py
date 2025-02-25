import pytest
from src.list_index_finder import find_first_index

def test_find_first_index_basic():
    """Test basic functionality of finding an index"""
    assert find_first_index([1, 2, 3, 4, 3], 3) == 2

def test_find_first_index_not_found():
    """Test when target is not in the list"""
    assert find_first_index([1, 2, 4, 5], 3) == -1

def test_find_first_index_empty_list():
    """Test with an empty list"""
    assert find_first_index([], 1) == -1

def test_find_first_index_first_occurrence():
    """Test that the first occurrence is returned"""
    assert find_first_index([3, 1, 3, 4, 3], 3) == 0

def test_find_first_index_single_element_list():
    """Test with a single-element list"""
    assert find_first_index([5], 5) == 0
    assert find_first_index([5], 6) == -1

def test_find_first_index_invalid_input():
    """Test with invalid input types"""
    assert find_first_index(None, 1) == -1
    assert find_first_index("not a list", 1) == -1