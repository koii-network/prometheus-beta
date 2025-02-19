import pytest
from src.max_subarray_sum import max_subarray_sum_constraint

def test_basic_case():
    # Basic case where solution exists
    A = [1, 2, 3, 4, 5]
    k = 2
    s = 9
    assert max_subarray_sum_constraint(A, k, s) == 12  # Subarray [3, 4, 5]

def test_no_valid_subarray():
    # Case where no subarray meets constraints
    A = [1, 2, 3]
    k = 3
    s = 10
    assert max_subarray_sum_constraint(A, k, s) == -1

def test_exact_minimum_length():
    # Case where subarray meets exactly minimum length
    A = [1, 2, 3, 4, 5]
    k = 3
    s = 10
    assert max_subarray_sum_constraint(A, k, s) == 12  # Subarray [3, 4, 5]

def test_multiple_possible_subarrays():
    # Case with multiple subarrays meeting constraints
    A = [2, 3, 4, 5, 6, 7]
    k = 2
    s = 10
    assert max_subarray_sum_constraint(A, k, s) == 18  # Subarray [5, 6, 7]

def test_array_too_short():
    # Case where array is shorter than minimum length
    A = [1, 2]
    k = 3
    s = 5
    assert max_subarray_sum_constraint(A, k, s) == -1

def test_negative_numbers():
    # Case with negative numbers
    A = [-1, -2, 3, 4, -5, 6, 7]
    k = 3
    s = 8
    assert max_subarray_sum_constraint(A, k, s) == 10  # Subarray [3, 4, -5, 6]

def test_edge_case_all_negative():
    # Case where all numbers are negative
    A = [-1, -2, -3, -4]
    k = 2
    s = -5
    assert max_subarray_sum_constraint(A, k, s) == -3  # Subarray [-1, -2]