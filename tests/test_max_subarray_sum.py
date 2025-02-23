import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with an array of mixed positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with an array of all negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    """Test with a single element array"""
    assert max_subarray_sum([42]) == 42

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")

def test_zero_sum_array():
    """Test an array with a zero sum"""
    assert max_subarray_sum([1, -1, 1, -1]) == 1