import pytest
from src.max_subarray import kadane_max_subarray

def test_positive_numbers():
    """Test with an array of positive numbers"""
    assert kadane_max_subarray([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert kadane_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with all negative numbers"""
    assert kadane_max_subarray([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test with a single element"""
    assert kadane_max_subarray([42]) == 42

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        kadane_max_subarray([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        kadane_max_subarray("not a list")

def test_large_numbers():
    """Test with large numbers"""
    assert kadane_max_subarray([1000000, -500000, 600000, -200000]) == 1100000

def test_zero_sum_subarray():
    """Test a case with zero sum subarray"""
    assert kadane_max_subarray([-1, 1, 0, -1, 1]) == 1