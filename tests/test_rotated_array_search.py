import pytest
from src.rotated_array_search import search_rotated_sorted_array

def test_search_rotated_sorted_array():
    # Test normal rotated array scenarios
    assert search_rotated_sorted_array([4,5,6,7,0,1,2], 0) == 4
    assert search_rotated_sorted_array([4,5,6,7,0,1,2], 3) == -1
    assert search_rotated_sorted_array([4,5,6,7,0,1,2], 5) == 1
    
    # Edge cases
    assert search_rotated_sorted_array([], 5) == -1  # Empty array
    assert search_rotated_sorted_array([1], 1) == 0  # Single element array
    assert search_rotated_sorted_array([1], 2) == -1  # Single element array, target not found
    
    # More complex rotation scenarios
    assert search_rotated_sorted_array([2,3,4,5,1], 1) == 4
    assert search_rotated_sorted_array([2,3,4,5,1], 2) == 0
    
    # No rotation (fully sorted array)
    assert search_rotated_sorted_array([1,2,3,4,5], 3) == 2
    assert search_rotated_sorted_array([1,2,3,4,5], 6) == -1