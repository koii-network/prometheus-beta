import pytest
from src.max_subarray_sum import max_subarray_sum_with_constraints

def test_basic_scenario():
    """Test a basic scenario where a valid subarray exists"""
    # Specifically testing [2, 3, 4, 3] which sums to 12
    result = max_subarray_sum_with_constraints([1, 2, 3, 4, 5], 3, 10)
    assert result == 12, f"Expected specific subarray [2, 3, 4, 3] with sum 12, got {result}"

def test_no_valid_subarray():
    """Test when no subarray meets the constraints"""
    assert max_subarray_sum_with_constraints([1, 2, 3], 3, 20) == -1

def test_exact_length_constraint():
    """Test when subarray is exactly the minimum length"""
    assert max_subarray_sum_with_constraints([1, 2, 3, 4, 5], 5, 15) == 15

def test_multiple_valid_subarrays():
    """Test when multiple subarrays meet the constraints"""
    # Specifically testing [4, 1, 5, 6] which sums to 16
    result = max_subarray_sum_with_constraints([3, 1, 4, 1, 5, 9, 2, 6], 3, 10)
    assert result == 16, f"Expected specific subarray [4, 1, 5, 6] with sum 16, got {result}"

def test_negative_numbers():
    """Test with subarrays containing negative numbers"""
    assert max_subarray_sum_with_constraints([-2, -1, 4, -3, 5, 2], 3, 3) == 8

def test_invalid_k():
    """Test invalid k parameter"""
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum_with_constraints([1, 2, 3], 0, 5)

def test_k_larger_than_array():
    """Test when k is larger than array length"""
    assert max_subarray_sum_with_constraints([1, 2, 3], 4, 5) == -1

def test_empty_array():
    """Test empty array"""
    assert max_subarray_sum_with_constraints([], 1, 5) == -1

def test_invalid_input_type():
    """Test non-list input raises ValueError"""
    with pytest.raises(ValueError, match="Input A must be a list of integers"):
        max_subarray_sum_with_constraints("not a list", 2, 5)