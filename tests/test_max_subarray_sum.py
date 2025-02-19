import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    """Test a normal case with a standard input"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    expected = [10, 23, 3, 1]
    assert max_subarray_sum(arr, k) == expected

def test_k_larger_than_array():
    """Test when k is larger than the array length"""
    arr = [1, 2, 3]
    k = 5
    assert max_subarray_sum(arr, k) == []

def test_zero_k():
    """Test when k is 0"""
    arr = [1, 2, 3, 4, 5]
    k = 0
    assert max_subarray_sum(arr, k) == []

def test_negative_k():
    """Test when k is negative"""
    arr = [1, 2, 3, 4, 5]
    k = -2
    assert max_subarray_sum(arr, k) == []

def test_single_element_array():
    """Test with a single element array"""
    arr = [5]
    k = 1
    assert max_subarray_sum(arr, k) == [5]

def test_all_same_elements():
    """Test an array with all same elements"""
    arr = [2, 2, 2, 2, 2]
    k = 3
    expected = [2, 2, 2]
    assert max_subarray_sum(arr, k) == expected

def test_mixed_positive_negative():
    """Test an array with mixed positive and negative numbers"""
    arr = [-1, 3, -4, 5, 1, -2, 4]
    k = 3
    expected = [5, 1, -2]
    assert max_subarray_sum(arr, k) == expected