import pytest
from src.max_sum_subarray import find_max_sum_subarray

def test_mixed_positive_negative():
    """Test array with mixed positive and negative numbers."""
    assert find_max_sum_subarray([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test array with all negative numbers."""
    assert find_max_sum_subarray([-1, -2, -3]) == -1

def test_empty_array():
    """Test empty array returns 0."""
    assert find_max_sum_subarray([]) == 0

def test_single_element_positive():
    """Test array with a single positive element."""
    assert find_max_sum_subarray([5]) == 5

def test_single_element_negative():
    """Test array with a single negative element."""
    assert find_max_sum_subarray([-5]) == -5

def test_all_positive_numbers():
    """Test array with all positive numbers."""
    assert find_max_sum_subarray([1, 2, 3, 4, 5]) == 15

def test_zero_sum_subarray():
    """Test array with a mix of positive and negative numbers that sum to 0."""
    assert find_max_sum_subarray([1, -1, 2, -2]) == 2

def test_multiple_max_sum_subarrays():
    """Test array with multiple potential maximum sum subarrays."""
    assert find_max_sum_subarray([1, 1, -2, 3, 4, -1, 3]) == 9

def test_large_numbers():
    """Test array with large numbers."""
    assert find_max_sum_subarray([10000, -5000, 20000, -15000]) == 25000