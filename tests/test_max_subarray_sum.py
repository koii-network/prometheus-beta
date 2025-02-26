import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_max_subarray_sum():
    """Test basic functionality of max_subarray_sum"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39

def test_all_same_elements():
    """Test array with all same elements"""
    arr = [5, 5, 5, 5, 5]
    k = 3
    assert max_subarray_sum(arr, k) == 15

def test_negative_numbers():
    """Test array with negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 2
    assert max_subarray_sum(arr, k) == -3

def test_mixed_numbers():
    """Test array with mixed positive and negative numbers"""
    arr = [1, -2, 3, 4, -5, 6, 7]
    k = 3
    assert max_subarray_sum(arr, k) == 12

def test_single_element():
    """Test array with single element and k=1"""
    arr = [42]
    k = 1
    assert max_subarray_sum(arr, k) == 42

def test_empty_array():
    """Test empty array"""
    arr = []
    k = 0
    assert max_subarray_sum(arr, k) == 0

def test_invalid_k_too_small():
    """Test k less than or equal to 0"""
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match="Subarray length \\(k\\) must be a positive integer"):
        max_subarray_sum(arr, 0)
    with pytest.raises(ValueError, match="Subarray length \\(k\\) must be a positive integer"):
        max_subarray_sum(arr, -1)

def test_invalid_k_too_large():
    """Test k greater than array length"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="Subarray length cannot be greater than array length"):
        max_subarray_sum(arr, 4)