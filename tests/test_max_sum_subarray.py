import pytest
from src.max_sum_subarray import maxSumSubarray

def test_max_sum_subarray_basic():
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 3
    assert maxSumSubarray(arr, k) == 33  # 10 + 23

def test_max_sum_subarray_whole_array():
    arr = [5, 2, 8, 1, 9]
    k = 5
    assert maxSumSubarray(arr, k) == 25

def test_max_sum_subarray_partial_overlap():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3
    assert maxSumSubarray(arr, k) == 24  # 7 + 8 + 9

def test_max_sum_subarray_negative_numbers():
    arr = [-1, -2, 3, -4, 5, -6, 7, -8, 9]
    k = 3
    assert maxSumSubarray(arr, k) == 12  # 5 + (-6) + 7

def test_max_sum_subarray_invalid_k_zero():
    with pytest.raises(ValueError, match="Subarray length \\(k\\) must be a positive integer"):
        maxSumSubarray([1, 2, 3], 0)

def test_max_sum_subarray_invalid_k_negative():
    with pytest.raises(ValueError, match="Subarray length \\(k\\) must be a positive integer"):
        maxSumSubarray([1, 2, 3], -1)

def test_max_sum_subarray_k_too_large():
    with pytest.raises(ValueError, match="Subarray length \\(k\\) cannot be greater than array length"):
        maxSumSubarray([1, 2, 3], 4)

def test_max_sum_subarray_empty_array():
    with pytest.raises(ValueError, match="Subarray length \\(k\\) cannot be greater than array length"):
        maxSumSubarray([], 1)