import pytest
from src.rotated_array_search import search_rotated_sorted_array

def test_search_rotated_sorted_array():
    # Test cases with different rotations and scenarios
    
    # Normal cases with target in the array
    assert search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 5) == 1
    assert search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 7) == 3
    
    # Edge cases
    assert search_rotated_sorted_array([1], 1) == 0
    assert search_rotated_sorted_array([1, 3], 3) == 1
    
    # Target not in array
    assert search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3) == -1
    
    # Empty array
    assert search_rotated_sorted_array([], 5) == -1
    
    # Fully sorted (not rotated) array
    assert search_rotated_sorted_array([1, 2, 3, 4, 5], 3) == 2
    
    # Array with rotation at different points
    assert search_rotated_sorted_array([5, 1, 2, 3, 4], 1) == 1
    assert search_rotated_sorted_array([3, 4, 5, 1, 2], 4) == 1

def test_search_rotated_sorted_array_error_cases():
    # Additional error and edge case handling
    
    # None input
    with pytest.raises(TypeError):
        search_rotated_sorted_array(None, 5)
    
    # Non-list input
    with pytest.raises(TypeError):
        search_rotated_sorted_array("not a list", 5)