import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with all positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with all negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test with a single element"""
    assert max_subarray_sum([42]) == 42

def test_empty_array_raises_error():
    """Test that empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        max_subarray_sum([])

def test_large_numbers():
    """Test with large numbers"""
    assert max_subarray_sum([10000, -5000, 3000, -1000, 500]) == 10000

def test_zero_sum_array():
    """Test an array with zero sum"""
    assert max_subarray_sum([-1, 1, 0, -1, 1]) == 1