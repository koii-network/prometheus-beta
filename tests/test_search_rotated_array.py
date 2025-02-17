import pytest
from src.search_rotated_array import search_rotated_sorted_array

def test_search_rotated_sorted_array_basic():
    # Basic scenario with rotated array
    arr = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated_sorted_array(arr, 0) == 4
    assert search_rotated_sorted_array(arr, 3) == -1

def test_search_rotated_sorted_array_edge_cases():
    # Empty array
    assert search_rotated_sorted_array([], 5) == -1
    
    # Single element array
    assert search_rotated_sorted_array([1], 1) == 0
    assert search_rotated_sorted_array([1], 0) == -1

def test_search_rotated_sorted_array_not_rotated():
    # Array not rotated
    arr = [1, 2, 3, 4, 5, 6, 7]
    assert search_rotated_sorted_array(arr, 3) == 2
    assert search_rotated_sorted_array(arr, 8) == -1

def test_search_rotated_sorted_array_rotated_at_start():
    # Array rotated at the start
    arr = [5, 6, 7, 8, 1, 2, 3, 4]
    assert search_rotated_sorted_array(arr, 1) == 4
    assert search_rotated_sorted_array(arr, 8) == 3

def test_search_rotated_sorted_array_all_elements():
    arr = [4, 5, 6, 7, 0, 1, 2]
    for i, num in enumerate(arr):
        assert search_rotated_sorted_array(arr, num) == i
    
    assert search_rotated_sorted_array(arr, 3) == -1