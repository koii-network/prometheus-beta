import pytest
from src.find_index import find_index

def test_find_index_basic():
    """Test finding an existing value in the list"""
    assert find_index([1, 2, 3, 4, 5], 3) == 2

def test_find_index_first_occurrence():
    """Test finding the first occurrence of a repeated value"""
    assert find_index([1, 2, 2, 3, 4], 2) == 1

def test_find_index_not_found():
    """Test when the target value is not in the list"""
    assert find_index([1, 2, 3, 4, 5], 6) == -1

def test_find_index_empty_list():
    """Test finding a value in an empty list"""
    assert find_index([], 1) == -1

def test_find_index_multiple_types():
    """Test finding a value when the list contains different types"""
    assert find_index([1, 'a', 2, 'b', 3], 'a') == 1

def test_find_index_edge_cases():
    """Test various edge cases"""
    # Finding first and last elements
    assert find_index([1, 2, 3, 4, 5], 1) == 0
    assert find_index([1, 2, 3, 4, 5], 5) == 4