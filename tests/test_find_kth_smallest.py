import pytest
from src.find_kth_smallest import find_kth_smallest

def test_find_kth_smallest_basic():
    """Test finding kth smallest in a basic scenario"""
    arr = [7, 10, 4, 3, 20, 15]
    assert find_kth_smallest(arr, 3) == 7

def test_find_kth_smallest_sorted():
    """Test finding kth smallest in an already sorted array"""
    arr = [1, 2, 3, 4, 5]
    assert find_kth_smallest(arr, 1) == 1
    assert find_kth_smallest(arr, 5) == 5

def test_find_kth_smallest_unsorted():
    """Test finding kth smallest in an unsorted array"""
    arr = [3, 1, 5, 12, 2, 11]
    assert find_kth_smallest(arr, 4) == 5

def test_find_kth_smallest_duplicate_elements():
    """Test array with duplicate elements"""
    arr = [3, 3, 1, 5, 1, 2]
    assert find_kth_smallest(arr, 3) == 2

def test_find_kth_smallest_invalid_k_too_low():
    """Test when k is less than 1"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        find_kth_smallest(arr, 0)

def test_find_kth_smallest_invalid_k_too_high():
    """Test when k is greater than array length"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        find_kth_smallest(arr, 4)

def test_find_kth_smallest_empty_array():
    """Test with an empty array"""
    arr = []
    with pytest.raises(ValueError, match="Array cannot be empty"):
        find_kth_smallest(arr, 1)

def test_find_kth_smallest_invalid_input_type():
    """Test with invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_kth_smallest("not a list", 1)
    
    with pytest.raises(TypeError, match="k must be an integer"):
        find_kth_smallest([1, 2, 3], "not an int")