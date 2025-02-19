import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_case():
    """Test with a standard array and valid k"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_single_element_array():
    """Test with a single element array"""
    arr = [5]
    assert max_subarray_sum(arr, 1) == 5

def test_k_larger_than_array():
    """Test when k is larger than the array length"""
    arr = [1, 2, 3]
    assert max_subarray_sum(arr, 4) is None

def test_k_equal_to_array_length():
    """Test when k is equal to the array length"""
    arr = [1, 2, 3, 4]
    assert max_subarray_sum(arr, 4) == 10

def test_negative_numbers():
    """Test with an array containing negative numbers"""
    arr = [-1, -4, -2, -10, -23, -3, -1, 0, -20]
    k = 3
    assert max_subarray_sum(arr, k) == -4  # Find the least negative subarray

def test_invalid_k_zero():
    """Test with k = 0"""
    arr = [1, 2, 3, 4]
    with pytest.raises(ValueError, match="Subarray size \\(k\\) must be a positive integer"):
        max_subarray_sum(arr, 0)

def test_invalid_k_negative():
    """Test with negative k"""
    arr = [1, 2, 3, 4]
    with pytest.raises(ValueError, match="Subarray size \\(k\\) must be a positive integer"):
        max_subarray_sum(arr, -1)

def test_empty_array():
    """Test with an empty array"""
    arr = []
    assert max_subarray_sum(arr, 1) is None