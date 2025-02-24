import pytest
from src.rotated_array_search import search_rotated_sorted_array

def test_search_rotated_sorted_array_basic():
    """Test basic functionality of searching in a rotated sorted array"""
    arr = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated_sorted_array(arr, 0) == 4
    assert search_rotated_sorted_array(arr, 3) == -1

def test_search_rotated_sorted_array_edge_cases():
    """Test edge cases"""
    # Empty array
    assert search_rotated_sorted_array([], 5) == -1
    
    # Single element array
    assert search_rotated_sorted_array([1], 1) == 0
    assert search_rotated_sorted_array([1], 2) == -1
    
    # No rotation
    arr = [1, 2, 3, 4, 5]
    assert search_rotated_sorted_array(arr, 3) == 2
    assert search_rotated_sorted_array(arr, 6) == -1

def test_search_rotated_sorted_array_full_rotation():
    """Test arrays fully rotated"""
    arr = [2, 3, 4, 5, 1]
    assert search_rotated_sorted_array(arr, 1) == 4
    assert search_rotated_sorted_array(arr, 2) == 0

def test_search_rotated_sorted_array_error_handling():
    """Test error handling for invalid inputs"""
    # Non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        search_rotated_sorted_array(123, 5)
    
    # Non-integer target
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_rotated_sorted_array([1, 2, 3], "5")

def test_search_rotated_sorted_array_duplicate_elements():
    """Test with arrays that may have duplicate elements"""
    arr = [2, 2, 2, 3, 4, 2]
    assert search_rotated_sorted_array(arr, 3) == 3
    assert search_rotated_sorted_array(arr, 5) == -1