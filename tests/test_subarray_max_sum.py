import pytest
from src.subarray_max_sum import maxSumSubarray

def test_basic_functionality():
    """Test basic functionality of maxSumSubarray"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert maxSumSubarray(arr, k) == 39  # Max sum is 10 + 23 + 3 + 1 = 39

def test_single_element_array():
    """Test array with a single element and k=1"""
    arr = [5]
    assert maxSumSubarray(arr, 1) == 5

def test_array_equal_to_k():
    """Test when k is equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert maxSumSubarray(arr, 5) == 15

def test_negative_numbers():
    """Test array with negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    assert maxSumSubarray(arr, 2) == -3

def test_mixed_numbers():
    """Test array with mixed positive and negative numbers"""
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    k = 3
    assert maxSumSubarray(arr, k) == 16  # 10 + (-4) + 7 = 16

def test_invalid_k_zero():
    """Test raising ValueError when k is zero"""
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        maxSumSubarray([1, 2, 3], 0)

def test_invalid_k_negative():
    """Test raising ValueError when k is negative"""
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        maxSumSubarray([1, 2, 3], -1)

def test_k_larger_than_array():
    """Test raising ValueError when k is larger than array length"""
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than the input array"):
        maxSumSubarray([1, 2, 3], 4)