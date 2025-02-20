import pytest
from src.longest_subarray import find_longest_abs_diff_subarray

def test_basic_functionality():
    # Basic test case
    assert find_longest_abs_diff_subarray([1, 5, 3, 8, 10], 2) == 4

def test_entire_array_valid():
    # All elements satisfy the condition
    assert find_longest_abs_diff_subarray([1, 4, 7, 11, 15], 3) == 5

def test_partial_array_valid():
    # Only part of the array satisfies the condition
    assert find_longest_abs_diff_subarray([1, 2, 5, 10, 1, 2, 3], 3) == 3

def test_single_element_array():
    # Single element array
    assert find_longest_abs_diff_subarray([5], 2) == 1

def test_empty_array():
    # Empty array
    assert find_longest_abs_diff_subarray([], 2) == 0

def test_negative_numbers():
    # Array with negative numbers
    assert find_longest_abs_diff_subarray([-1, -4, -7, -10], 3) == 4

def test_mixed_numbers():
    # Array with mixed positive and negative numbers
    assert find_longest_abs_diff_subarray([-5, 3, 7, 1, 10], 4) == 3

def test_invalid_input_type():
    # Test invalid input types
    with pytest.raises(ValueError, match="Input must be a list of integers"):
        find_longest_abs_diff_subarray(123, 2)
    
    with pytest.raises(ValueError, match="k must be an integer"):
        find_longest_abs_diff_subarray([1, 2, 3], "2")

def test_k_zero():
    # Test when k is zero
    assert find_longest_abs_diff_subarray([1, 1, 2, 2, 3, 3], 0) == 6

def test_large_k():
    # Test when k is larger than possible differences
    assert find_longest_abs_diff_subarray([1, 2, 3, 4, 5], 10) == 1