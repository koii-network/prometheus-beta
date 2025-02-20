import pytest
from src.max_subarray_sum import max_subarray_sum

def test_max_subarray_sum_basic():
    """Test basic functionality with a standard array"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_max_subarray_sum_single_element():
    """Test with an array of single elements and different k values"""
    arr = [5]
    assert max_subarray_sum(arr, 1) == 5

def test_max_subarray_sum_negative_numbers():
    """Test with negative numbers in the array"""
    arr = [-1, -2, -3, -4, -5]
    k = 2
    assert max_subarray_sum(arr, k) == -3  # -1 + -2 = -3

def test_max_subarray_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    arr = [1, -3, 4, 5, -2, 3, 6]
    k = 3
    assert max_subarray_sum(arr, k) == 12  # 4 + 5 + (-2) or 5 + (-2) + 3 or (-2) + 3 + 6

def test_max_subarray_sum_invalid_k_zero():
    """Test with k = 0, should raise ValueError"""
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        max_subarray_sum(arr, 0)

def test_max_subarray_sum_invalid_k_large():
    """Test with k larger than array length, should raise ValueError"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than the array length"):
        max_subarray_sum(arr, 4)

def test_max_subarray_sum_empty_array():
    """Test with an empty array, should handle it gracefully"""
    arr = []
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than the array length"):
        max_subarray_sum(arr, 1)