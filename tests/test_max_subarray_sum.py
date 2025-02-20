import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_case():
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1

def test_single_element_array():
    arr = [5]
    k = 1
    assert max_subarray_sum(arr, k) == 5

def test_all_same_elements():
    arr = [2, 2, 2, 2, 2]
    k = 3
    assert max_subarray_sum(arr, k) == 6

def test_negative_numbers():
    arr = [-1, -2, -3, -4, -5]
    k = 2
    assert max_subarray_sum(arr, k) == -3  # -1 + -2

def test_mixed_numbers():
    arr = [1, -2, 3, 4, -1, 5, -3]
    k = 3
    assert max_subarray_sum(arr, k) == 10  # 3 + 4 + -1

def test_invalid_k_too_large():
    arr = [1, 2, 3]
    k = 4
    with pytest.raises(ValueError, match="Subarray length \\(k\\) cannot be larger than array length"):
        max_subarray_sum(arr, k)

def test_invalid_k_too_small():
    arr = [1, 2, 3]
    k = 0
    with pytest.raises(ValueError, match="Subarray length \\(k\\) must be at least 1"):
        max_subarray_sum(arr, k)

def test_empty_array():
    arr = []
    k = 0
    assert max_subarray_sum(arr, k) == 0