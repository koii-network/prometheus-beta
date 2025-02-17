import pytest
from src.rotated_array_search import search_rotated_array

def test_search_rotated_array_basic():
    # Basic rotation case
    arr = [4, 5, 6, 7, 0, 1, 2]
    
    # Test searching for existing elements
    assert search_rotated_array(arr, 0) == 4
    assert search_rotated_array(arr, 6) == 2
    assert search_rotated_array(arr, 2) == 6
    
    # Test searching for non-existing elements
    assert search_rotated_array(arr, 3) == -1
    assert search_rotated_array(arr, 8) == -1

def test_search_rotated_array_edge_cases():
    # Empty array
    assert search_rotated_array([], 5) == -1
    
    # Single element array
    assert search_rotated_array([1], 1) == 0
    assert search_rotated_array([1], 2) == -1
    
    # No rotation array
    arr_no_rotation = [1, 2, 3, 4, 5]
    assert search_rotated_array(arr_no_rotation, 3) == 2
    assert search_rotated_array(arr_no_rotation, 6) == -1

def test_search_rotated_array_various_rotations():
    # Various rotation scenarios
    cases = [
        ([5, 6, 7, 8, 1, 2, 3, 4], 1, 4),  # Mid rotation
        ([3, 4, 5, 1, 2], 1, 3),  # Smaller rotation
        ([2, 3, 4, 5, 1], 1, 4),  # Another rotation case
    ]
    
    for arr, target, expected_index in cases:
        assert search_rotated_array(arr, target) == expected_index