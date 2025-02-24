import pytest
from src.subarray_max_diff import longest_subarray_with_max_diff

def test_basic_cases():
    # Test basic scenarios with various inputs
    assert longest_subarray_with_max_diff([1, 2, 3, 4], 1) == 4
    assert longest_subarray_with_max_diff([1, 3, 6, 10], 3) == 3
    assert longest_subarray_with_max_diff([2, 5, 8, 12], 3) == 4

def test_single_element_array():
    # Test single element array always returns 1
    assert longest_subarray_with_max_diff([5], 0) == 1
    assert longest_subarray_with_max_diff([10], 2) == 1

def test_non_continuous_max_diff():
    # Test scenarios where max subarray is not continuous
    assert longest_subarray_with_max_diff([1, 5, 3, 6, 7], 2) == 3
    assert longest_subarray_with_max_diff([1, 4, 2, 5, 3], 1) == 3

def test_edge_cases():
    # Test various edge cases
    assert longest_subarray_with_max_diff([1, 1, 1, 1], 0) == 4
    assert longest_subarray_with_max_diff([1, 2, 1, 2], 1) == 2

def test_error_cases():
    # Test error handling
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        longest_subarray_with_max_diff([], 1)
    
    with pytest.raises(ValueError, match="Difference k must be non-negative"):
        longest_subarray_with_max_diff([1, 2, 3], -1)

def test_negative_numbers():
    # Test scenarios with negative numbers
    assert longest_subarray_with_max_diff([-1, -4, -7, -10], 2) == 4
    assert longest_subarray_with_max_diff([-1, 2, -3, 4], 3) == 3