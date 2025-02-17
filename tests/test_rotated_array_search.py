import pytest
from src.rotated_array_search import search_rotated_sorted_array

def test_normal_rotated_array():
    arr = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated_sorted_array(arr, 0) == 4
    assert search_rotated_sorted_array(arr, 3) == -1

def test_minimal_rotations():
    # Array rotated just a bit
    arr = [7, 0, 1, 2, 4, 5, 6]
    assert search_rotated_sorted_array(arr, 0) == 1
    assert search_rotated_sorted_array(arr, 6) == 6

def test_no_rotation():
    # Completely sorted array
    arr = [0, 1, 2, 4, 5, 6, 7]
    assert search_rotated_sorted_array(arr, 4) == 3
    assert search_rotated_sorted_array(arr, 8) == -1

def test_edge_cases():
    # Empty array
    assert search_rotated_sorted_array([], 5) == -1
    
    # Single element array
    assert search_rotated_sorted_array([1], 1) == 0
    assert search_rotated_sorted_array([1], 0) == -1

def test_duplicate_elements_not_guaranteed():
    # While the function assumes no duplicates, test some scenarios
    arr = [2, 3, 4, 5, 1]
    assert search_rotated_sorted_array(arr, 1) == 4