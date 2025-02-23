import pytest
from src.max_subarray_sum import max_subarray_sum_with_constraints

def test_basic_case():
    """Test a basic scenario with a valid subarray"""
    A = [1, 2, 3, 4, 5]
    k = 2
    s = 10
    result = max_subarray_sum_with_constraints(A, k, s)
    assert result >= 9, f"Expected sum >= 9, got {result}"

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
    result = max_subarray_sum_with_constraints(A, k, s)
    assert result >= 15, f"Expected sum >= 15, got {result}"

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
    result = max_subarray_sum_with_constraints(A, k, s)
    assert result >= 7, f"Expected sum >= 7, got {result}"

def test_exact_length_and_sum():
    """Test subarray that exactly meets length and sum requirements"""
    A = [1, 2, 3, 4, 5]
    k = 3
    s = 9
    result = max_subarray_sum_with_constraints(A, k, s)
    assert result >= 12, f"Expected sum >= 12, got {result}"

def test_large_numbers():
    """Test with large numbers"""
    A = [1000, 2000, 3000, 4000, 5000]
    k = 2
    s = 7000
    result = max_subarray_sum_with_constraints(A, k, s)
    assert result >= 9000, f"Expected sum >= 9000, got {result}"