import pytest
from src.search_rotated_array import search_rotated_sorted_array

def test_search_rotated_sorted_array():
    # Test case: Basic rotated array, target exists
    assert search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3) == -1
    
    # Test case: Array not rotated
    assert search_rotated_sorted_array([1, 2, 3, 4, 5], 3) == 2
    
    # Test case: Completely rotated array
    assert search_rotated_sorted_array([2, 3, 4, 5, 1], 1) == 4
    
    # Test case: Empty array
    assert search_rotated_sorted_array([], 5) == -1
    
    # Test case: Single element array
    assert search_rotated_sorted_array([1], 1) == 0
    assert search_rotated_sorted_array([1], 2) == -1
    
    # Test case: Repeated elements
    assert search_rotated_sorted_array([2, 2, 2, 3, 4, 2], 3) == 3