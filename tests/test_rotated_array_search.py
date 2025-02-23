import pytest
from src.rotated_array_search import search_rotated_array

def test_basic_rotated_array_search():
    """Test searching in a basic rotated sorted array"""
    arr = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated_array(arr, 0) == 4
    assert search_rotated_array(arr, 3) == -1

def test_edge_cases():
    """Test various edge cases"""
    # Empty array
    assert search_rotated_array([], 5) == -1
    
    # Single element array
    assert search_rotated_array([1], 1) == 0
    assert search_rotated_array([1], 0) == -1
    
    # No rotation
    arr = [1, 2, 3, 4, 5]
    assert search_rotated_array(arr, 3) == 2
    assert search_rotated_array(arr, 6) == -1

def test_multiple_rotations():
    """Test arrays with different rotation points"""
    # Rotated multiple times
    arr1 = [7, 8, 1, 2, 3, 4, 5, 6]
    assert search_rotated_array(arr1, 8) == 1
    assert search_rotated_array(arr1, 3) == 4
    
    # Another rotation scenario
    arr2 = [2, 3, 4, 5, 6, 7, 8, 1]
    assert search_rotated_array(arr2, 1) == 7
    assert search_rotated_array(arr2, 5) == 3

def test_duplicates():
    """Ensure the function handles cases with potential duplicates correctly"""
    arr = [2, 2, 2, 3, 2, 2]
    # Note: While the current implementation might not handle all duplicate cases perfectly,
    # it should still work for many scenarios
    assert search_rotated_array(arr, 3) == 3
    assert search_rotated_array(arr, 1) == -1