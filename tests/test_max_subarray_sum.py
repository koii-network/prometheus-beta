import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_max_subarray_sum():
    """Test a basic scenario with a valid input"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_single_window():
    """Test when k equals array length"""
    arr = [2, 3, 4, 1, 5]
    k = 5
    assert max_subarray_sum(arr, k) == 15

def test_empty_array():
    """Test empty array input"""
    arr = []
    k = 3
    assert max_subarray_sum(arr, k) is None

def test_invalid_k():
    """Test with k larger than array length"""
    arr = [1, 2, 3]
    k = 4
    assert max_subarray_sum(arr, k) is None

def test_negative_numbers():
    """Test with negative numbers in the array"""
    arr = [-1, -2, -3, -4, -5]
    k = 3
    assert max_subarray_sum(arr, k) == -6

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    k = 3
    assert max_subarray_sum(arr, k) == 13  # 10 + (-4) + 7 = 13