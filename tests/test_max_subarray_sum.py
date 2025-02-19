import pytest
from src.max_subarray_sum import max_subarray_sum_with_constraints

def test_basic_valid_subarray():
    A = [1, 2, 3, 4, 5]
    k = 2  # minimum 2 elements
    s = 9  # sum at least 9
    assert max_subarray_sum_with_constraints(A, k, s) == 9

def test_no_valid_subarray_exists():
    A = [1, 2, 3]
    k = 2
    s = 10
    assert max_subarray_sum_with_constraints(A, k, s) == -1

def test_exact_minimum_length():
    A = [5, 5, 5]
    k = 3  # exactly 3 elements
    s = 15
    assert max_subarray_sum_with_constraints(A, k, s) == 15

def test_multiple_valid_subarrays():
    A = [1, 4, 3, 2, 6]
    k = 2
    s = 10
    assert max_subarray_sum_with_constraints(A, k, s) == 12

def test_empty_array():
    A = []
    k = 2
    s = 5
    assert max_subarray_sum_with_constraints(A, k, s) == -1

def test_k_greater_than_array_length():
    A = [1, 2, 3]
    k = 4
    s = 5
    assert max_subarray_sum_with_constraints(A, k, s) == -1

def test_negative_numbers():
    A = [-1, -2, 3, 4, -5, 6]
    k = 2
    s = 5
    assert max_subarray_sum_with_constraints(A, k, s) == 7