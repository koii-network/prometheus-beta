import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_functionality():
    """Test basic functionality with a simple array"""
    arr = [1, 2, 3, 4, 5]
    k = 3
    assert max_subarray_sum(arr, k) == 12  # 3 + 4 + 5

def test_entire_array():
    """Test when k is the entire array length"""
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert max_subarray_sum(arr, k) == 15

def test_single_element():
    """Test with k = 1"""
    arr = [1, 2, 3, 4, 5]
    k = 1
    assert max_subarray_sum(arr, k) == 5

def test_invalid_k_larger_than_array():
    """Test when k is larger than array length"""
    arr = [1, 2, 3]
    k = 4
    assert max_subarray_sum(arr, k) is None

def test_invalid_k_zero():
    """Test when k is zero"""
    arr = [1, 2, 3]
    k = 0
    assert max_subarray_sum(arr, k) is None

def test_invalid_k_negative():
    """Test when k is negative"""
    arr = [1, 2, 3]
    k = -1
    assert max_subarray_sum(arr, k) is None

def test_mixed_array():
    """Test with mixed positive and negative numbers"""
    arr = [-1, 2, -3, 4, 5, -6]
    k = 3
    assert max_subarray_sum(arr, k) == 6  # 4 + 5 + (-3)

def test_empty_array():
    """Test with an empty array"""
    arr = []
    k = 1
    assert max_subarray_sum(arr, k) is None