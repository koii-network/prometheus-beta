import pytest
from src.max_subarray_sum import max_subarray_sum

def test_valid_subarray_sum():
    # Basic test case
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_all_positive_numbers():
    arr = [100, 200, 300, 400, 500]
    k = 3
    assert max_subarray_sum(arr, k) == 1200  # 300 + 400 + 500 = 1200

def test_mixed_numbers():
    arr = [-1, 5, 3, -2, 4, -1, 2]
    k = 3
    assert max_subarray_sum(arr, k) == 9  # 5 + 3 - 2 = 6

def test_k_equals_array_length():
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert max_subarray_sum(arr, k) == 15  # sum of entire array

def test_empty_array():
    arr = []
    k = 3
    assert max_subarray_sum(arr, k) is None

def test_k_exceeds_array_length():
    arr = [1, 2, 3]
    k = 4
    assert max_subarray_sum(arr, k) is None

def test_invalid_k():
    arr = [1, 2, 3, 4, 5]
    k = 0
    assert max_subarray_sum(arr, k) is None

def test_single_element_array():
    arr = [42]
    k = 1
    assert max_subarray_sum(arr, k) == 42