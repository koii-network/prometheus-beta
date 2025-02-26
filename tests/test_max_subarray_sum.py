import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_max_subarray_sum():
    """Test basic functionality with a standard array"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_all_positive_numbers():
    """Test max subarray sum with all positive numbers"""
    arr = [5, 2, 7, 3, 1, 9, 4]
    k = 3
    assert max_subarray_sum(arr, k) == 20  # 7 + 3 + 1 = 11

def test_all_negative_numbers():
    """Test max subarray sum with all negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 3
    assert max_subarray_sum(arr, k) == -6  # -1 + -2 + -3 = -6

def test_mixed_numbers():
    """Test max subarray sum with mixed positive and negative numbers"""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    k = 4
    assert max_subarray_sum(arr, k) == 6  # 4 + -1 + 2 + 1 = 6

def test_k_equals_array_length():
    """Test when k is equal to the array length"""
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert max_subarray_sum(arr, k) == 15

def test_invalid_k_zero():
    """Test raising ValueError when k is zero"""
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum([1, 2, 3], 0)

def test_invalid_k_negative():
    """Test raising ValueError when k is negative"""
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum([1, 2, 3], -1)

def test_invalid_k_larger_than_array():
    """Test raising ValueError when k is larger than array length"""
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum([1, 2, 3], 4)

def test_empty_array():
    """Test raising ValueError for an empty array"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        max_subarray_sum([], 1)

def test_single_element_array():
    """Test single element array with k=1"""
    arr = [42]
    k = 1
    assert max_subarray_sum(arr, k) == 42