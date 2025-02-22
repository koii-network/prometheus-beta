import pytest
from src.search_rotated_array import search_rotated_sorted_array

def test_search_rotated_sorted_array():
    # Test various scenarios
    
    # Normal rotation scenarios
    assert search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3) == -1
    
    # No rotation scenarios
    assert search_rotated_sorted_array([1, 2, 3, 4, 5], 3) == 2
    assert search_rotated_sorted_array([1, 2, 3, 4, 5], 6) == -1
    
    # Edge cases
    assert search_rotated_sorted_array([], 5) == -1  # Empty array
    assert search_rotated_sorted_array([1], 1) == 0  # Single element array
    assert search_rotated_sorted_array([1], 2) == -1  # Single element array, different target
    
    # Rotation at different points
    assert search_rotated_sorted_array([5, 1, 2, 3, 4], 1) == 1
    assert search_rotated_sorted_array([3, 4, 5, 1, 2], 1) == 3

def test_multiple_elements_with_same_value():
    # Since the problem statement suggests unique elements, 
    # this is an edge case where behavior might not be guaranteed
    result = search_rotated_sorted_array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 2)
    assert result != -1  # Should find at least one occurrence

def test_large_rotated_array():
    large_arr = list(range(10000, 20000)) + list(range(0, 10000))
    assert search_rotated_sorted_array(large_arr, 15000) != -1
    assert search_rotated_sorted_array(large_arr, 25000) == -1