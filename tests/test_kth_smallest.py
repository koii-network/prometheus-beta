import pytest
from src.kth_smallest import find_kth_smallest

def test_find_kth_smallest_basic():
    """Test basic functionality of finding kth smallest element"""
    arr = [7, 10, 4, 3, 20, 15]
    assert find_kth_smallest(arr, 3) == 7
    assert find_kth_smallest(arr, 1) == 3
    assert find_kth_smallest(arr, 6) == 20

def test_find_kth_smallest_with_duplicates():
    """Test finding kth smallest with duplicate elements"""
    arr = [7, 7, 10, 4, 3, 20, 15, 3]
    assert find_kth_smallest(arr, 3) == 4
    assert find_kth_smallest(arr, 1) == 3

def test_find_kth_smallest_single_element():
    """Test with a single-element array"""
    arr = [42]
    assert find_kth_smallest(arr, 1) == 42

def test_find_kth_smallest_invalid_k():
    """Test invalid k values"""
    arr = [7, 10, 4, 3, 20, 15]
    
    with pytest.raises(ValueError, match="k must be between 1 and 6"):
        find_kth_smallest(arr, 0)
    
    with pytest.raises(ValueError, match="k must be between 1 and 6"):
        find_kth_smallest(arr, 7)

def test_find_kth_smallest_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_kth_smallest(42, 1)
    
    with pytest.raises(TypeError, match="k must be an integer"):
        find_kth_smallest([1, 2, 3], "2")