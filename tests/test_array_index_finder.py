import pytest
from src.array_index_finder import find_first_index

def test_find_first_index_basic():
    """Test basic functionality of finding an index"""
    assert find_first_index([1, 2, 3, 4, 3], 3) == 2

def test_find_first_index_not_found():
    """Test when target is not in the array"""
    assert find_first_index([1, 2, 3, 4], 5) == -1

def test_find_first_index_empty_array():
    """Test with an empty array"""
    assert find_first_index([], 1) == -1

def test_find_first_index_first_occurrence():
    """Test that the first occurrence is returned"""
    assert find_first_index([1, 2, 2, 3, 2], 2) == 1

def test_find_first_index_different_types():
    """Test with different types of values"""
    assert find_first_index([1, 'a', True, None, 'a'], 'a') == 1

def test_find_first_index_none():
    """Test finding None as a target"""
    assert find_first_index([1, None, 2, None], None) == 1