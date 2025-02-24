import pytest
from src.rotated_array_search import search_rotated_array

def test_search_rotated_array_basic():
    """Test basic functionality of search_rotated_array"""
    arr = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated_array(arr, 0) == 4
    assert search_rotated_array(arr, 3) == -1

def test_search_rotated_array_edge_cases():
    """Test edge cases of search_rotated_array"""
    # Empty array
    assert search_rotated_array([], 5) == -1
    
    # Single element array
    assert search_rotated_array([1], 1) == 0
    assert search_rotated_array([1], 0) == -1
    
    # Not rotated array
    arr = [0, 1, 2, 3, 4, 5]
    assert search_rotated_array(arr, 3) == 3
    assert search_rotated_array(arr, 6) == -1

def test_search_rotated_array_boundary_conditions():
    """Test boundary conditions of search_rotated_array"""
    # Rotated at first/last elements
    arr1 = [2, 3, 4, 5, 1]
    assert search_rotated_array(arr1, 1) == 4
    assert search_rotated_array(arr1, 2) == 0
    
    arr2 = [5, 1, 2, 3, 4]
    assert search_rotated_array(arr2, 5) == 0
    assert search_rotated_array(arr2, 3) == 3

def test_search_rotated_array_error_handling():
    """Test error handling of search_rotated_array"""
    # Invalid input types
    with pytest.raises(TypeError, match="Input must be a list"):
        search_rotated_array("not a list", 5)
    
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_rotated_array([1, 2, 3], "5")

def test_search_rotated_array_duplicate_free():
    """Ensure function works with arrays without duplicates"""
    arr = [4, 5, 6, 7, 0, 1, 2]
    for i, num in enumerate(arr):
        assert search_rotated_array(arr, num) == i
    
    assert search_rotated_array(arr, 8) == -1