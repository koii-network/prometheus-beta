import pytest
from src.max_sum_subarray import maxSumSubarray

def test_basic_max_sum_subarray():
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert maxSumSubarray(arr, k) == 39  # 10 + 23 + 3 + 1

def test_max_sum_subarray_single_element():
    arr = [5, 2, 3, 4, 1]
    k = 1
    assert maxSumSubarray(arr, k) == 5

def test_max_sum_subarray_entire_array():
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert maxSumSubarray(arr, k) == 15

def test_max_sum_subarray_negative_numbers():
    arr = [-1, -2, 3, 4, -5, 6, 7]
    k = 3
    assert maxSumSubarray(arr, k) == 8  # Adjusted to match actual expected result

def test_max_sum_invalid_k_zero():
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        maxSumSubarray(arr, 0)

def test_max_sum_invalid_k_negative():
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        maxSumSubarray(arr, -1)

def test_max_sum_invalid_k_too_large():
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than the array length"):
        maxSumSubarray(arr, 4)

def test_max_sum_empty_array():
    arr = []
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than the array length"):
        maxSumSubarray(arr, 1)