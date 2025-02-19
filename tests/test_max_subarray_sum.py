import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_subarray_sum():
    """Test basic functionality of max_subarray_sum"""
    nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(nums, k) == [10, 23, 3, 1]

def test_empty_list():
    """Test with an empty list"""
    nums = []
    k = 3
    assert max_subarray_sum(nums, k) == []

def test_k_larger_than_list():
    """Test when k is larger than list length"""
    nums = [1, 2, 3]
    k = 5
    assert max_subarray_sum(nums, k) == []

def test_k_zero():
    """Test when k is zero"""
    nums = [1, 2, 3, 4, 5]
    k = 0
    assert max_subarray_sum(nums, k) == []

def test_k_negative():
    """Test when k is negative"""
    nums = [1, 2, 3, 4, 5]
    k = -1
    assert max_subarray_sum(nums, k) == []

def test_single_max_window():
    """Test with a list where only one window exists"""
    nums = [1, 2, 3]
    k = 3
    assert max_subarray_sum(nums, k) == [1, 2, 3]

def test_multiple_equal_windows():
    """Test with multiple windows having the same sum"""
    nums = [1, 1, 1, 2, 2, 2, 1, 1, 1]
    k = 3
    assert max_subarray_sum(nums, k) in [[2, 2, 2], [1, 2, 2], [2, 2, 1]]