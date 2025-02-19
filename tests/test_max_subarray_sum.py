import pytest
from src.max_subarray_sum import max_subarray_sum_with_constraints

def test_basic_case():
    A = [1, 2, 3, 4, 5]
    assert max_subarray_sum_with_constraints(A, 2, 7) == 9  # [2,3,4]

def test_no_valid_subarray():
    A = [1, 2, 3]
    assert max_subarray_sum_with_constraints(A, 3, 20) == -1

def test_exact_minimum_length():
    A = [1, 2, 3, 4, 5]
    assert max_subarray_sum_with_constraints(A, 2, 5) == 9  # [2,3,4]

def test_multiple_valid_subarrays():
    A = [2, 3, 1, 4, 5, 6]
    assert max_subarray_sum_with_constraints(A, 3, 10) == 15  # [4,5,6]

def test_negative_numbers():
    A = [-1, -2, 3, 4, -5, 6, 7]
    assert max_subarray_sum_with_constraints(A, 3, 8) == 13  # [3,4,6]

def test_all_small_numbers():
    A = [1, 1, 1, 1, 1]
    assert max_subarray_sum_with_constraints(A, 3, 3) == 3

def test_array_smaller_than_k():
    A = [1, 2]
    assert max_subarray_sum_with_constraints(A, 3, 5) == -1

def test_empty_array():
    A = []
    assert max_subarray_sum_with_constraints(A, 2, 5) == -1