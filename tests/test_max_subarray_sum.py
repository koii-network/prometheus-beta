import pytest
from src.max_subarray_sum import max_subarray_sum_with_constraints

def test_basic_case():
    """Test a basic scenario with a valid subarray"""
    A = [1, 2, 3, 4, 5]
    k = 2
    s = 10
    assert max_subarray_sum_with_constraints(A, k, s) in [9, 12]  # 3+4+5 or 4+5

def test_no_valid_subarray():
    """Test when no subarray meets the constraints"""
    A = [1, 2, 3, 4, 5]
    k = 3
    s = 20
    assert max_subarray_sum_with_constraints(A, k, s) == -1

def test_multiple_valid_subarrays():
    """Test case with multiple valid subarrays"""
    A = [2, 3, 1, 4, 5, 6]
    k = 3
    s = 10
    assert max_subarray_sum_with_constraints(A, k, s) in [15, 16]  # 4+5+6 or 2+3+1+4+5

def test_single_element_array():
    """Test with a single element array"""
    A = [5]
    k = 1
    s = 5
    assert max_subarray_sum_with_constraints(A, k, s) == 5

def test_empty_array():
    """Test an empty array"""
    A = []
    k = 2
    s = 10
    assert max_subarray_sum_with_constraints(A, k, s) == -1

def test_invalid_k():
    """Test with invalid k values"""
    A = [1, 2, 3, 4, 5]
    assert max_subarray_sum_with_constraints(A, 0, 10) == -1
    assert max_subarray_sum_with_constraints(A, 6, 10) == -1

def test_negative_elements():
    """Test with negative elements"""
    A = [-1, -2, 3, 4, -5, 6]
    k = 3
    s = 5
    assert max_subarray_sum_with_constraints(A, k, s) in [7, 8]  # 3+4 or 3+4+1

def test_exact_length_and_sum():
    """Test subarray that exactly meets length and sum requirements"""
    A = [1, 2, 3, 4, 5]
    k = 3
    s = 9
    assert max_subarray_sum_with_constraints(A, k, s) in [12, 14]  # 3+4+5 or 1+2+3+4+5

def test_large_numbers():
    """Test with large numbers"""
    A = [1000, 2000, 3000, 4000, 5000]
    k = 2
    s = 7000
    assert max_subarray_sum_with_constraints(A, k, s) in [9000, 12000]  # 4000+5000 or 3000+4000+5000