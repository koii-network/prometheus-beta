import pytest
from src.max_subarray_sum import max_subarray_sum

def test_max_subarray_sum_normal_case():
    """Test a standard case with clear maximum subarray"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == [10, 23, 3, 1]

def test_max_subarray_sum_all_same_elements():
    """Test case where all elements are the same"""
    arr = [5, 5, 5, 5, 5, 5]
    k = 3
    assert max_subarray_sum(arr, k) == [5, 5, 5]

def test_max_subarray_sum_negative_numbers():
    """Test case with negative numbers"""
    arr = [-1, -4, -2, -10, -23, -3, -1, -20]
    k = 3
    assert max_subarray_sum(arr, k) == [-1, -4, -2]

def test_max_subarray_sum_k_larger_than_array():
    """Test when k is larger than array length"""
    arr = [1, 2, 3]
    k = 5
    assert max_subarray_sum(arr, k) == []

def test_max_subarray_sum_zero_k():
    """Test when k is zero"""
    arr = [1, 2, 3, 4, 5]
    k = 0
    assert max_subarray_sum(arr, k) == []

def test_max_subarray_sum_single_element():
    """Test with single element array"""
    arr = [42]
    k = 1
    assert max_subarray_sum(arr, k) == [42]

def test_max_subarray_sum_multiple_max_possible():
    """Test case where multiple subarrays have same max sum"""
    arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    k = 4
    result = max_subarray_sum(arr, k)
    assert result == [2, 3, 4, 5] or result == [1, 2, 3, 4]