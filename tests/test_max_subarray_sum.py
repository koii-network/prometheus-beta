import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    """Test a normal case with a valid subarray length"""
    assert max_subarray_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == [39]

def test_entire_list():
    """Test when k equals the entire list length"""
    assert max_subarray_sum([1, 2, 3, 4, 5], 5) == [15]

def test_empty_list():
    """Test with an empty list"""
    assert max_subarray_sum([], 3) == []

def test_k_larger_than_list():
    """Test when k is larger than the list length"""
    assert max_subarray_sum([1, 2, 3], 5) == []

def test_single_element_list():
    """Test with a single element list"""
    assert max_subarray_sum([5], 1) == [5]

def test_negative_numbers():
    """Test with negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4, -5], 2) == [-3]

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert max_subarray_sum([1, -1, 5, -2, 3, 10, -5], 3) == [18]]