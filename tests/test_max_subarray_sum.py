import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    assert max_subarray_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39

def test_k_larger_than_list():
    assert max_subarray_sum([1, 2, 3], 5) == []

def test_k_zero():
    assert max_subarray_sum([1, 2, 3, 4, 5], 0) == []

def test_single_element_list():
    assert max_subarray_sum([5], 1) == 5

def test_negative_numbers():
    assert max_subarray_sum([-1, -2, -3, -4, -5], 2) == -3

def test_mixed_numbers():
    assert max_subarray_sum([-1, 2, 3, -4, 5, 6, -7], 3) == 7

def test_empty_list():
    assert max_subarray_sum([], 2) == []