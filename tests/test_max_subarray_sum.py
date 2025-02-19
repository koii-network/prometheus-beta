import pytest
from src.max_subarray_sum import max_subarray_sum

def test_max_subarray_sum_positive_numbers():
    """Test with all positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_max_subarray_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_sum_all_negative():
    """Test with all negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_max_subarray_sum_single_element():
    """Test with a single element"""
    assert max_subarray_sum([5]) == 5

def test_max_subarray_sum_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        max_subarray_sum([])