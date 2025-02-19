import pytest
from src.kadane_algorithm import max_subarray_sum

def test_max_subarray_sum_positive_numbers():
    """Test with an array of positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_max_subarray_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_sum_negative_numbers():
    """Test with an array of only negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_max_subarray_sum_single_element():
    """Test with a single element"""
    assert max_subarray_sum([42]) == 42

def test_max_subarray_sum_empty_list():
    """Test raising an error for an empty list"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_max_subarray_sum_invalid_input():
    """Test raising an error for invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")