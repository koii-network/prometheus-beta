import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_max_subarray_sum():
    """Test basic functionality with a typical array"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_k_equal_to_array_length():
    """Test when k is equal to the entire array length"""
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert max_subarray_sum(arr, k) == sum(arr)

def test_single_element_array():
    """Test array with a single element"""
    arr = [42]
    k = 1
    assert max_subarray_sum(arr, k) == 42

def test_all_negative_numbers():
    """Test array with all negative numbers"""
    arr = [-1, -3, -2, -4, -5]
    k = 3
    assert max_subarray_sum(arr, k) == -6  # -1 + -3 + -2 = -6

def test_mixed_positive_negative():
    """Test array with mixed positive and negative numbers"""
    arr = [3, -1, 4, -2, 5, -3]
    k = 3
    assert max_subarray_sum(arr, k) == 7  # 3 + -1 + 5 = 7

def test_invalid_k_zero():
    """Test raising ValueError when k is zero"""
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum([1, 2, 3], 0)

def test_invalid_k_negative():
    """Test raising ValueError when k is negative"""
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum([1, 2, 3], -1)

def test_invalid_k_too_large():
    """Test raising ValueError when k is larger than array length"""
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum([1, 2, 3], 4)

def test_empty_array():
    """Test empty array with any valid k"""
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum([], 1)