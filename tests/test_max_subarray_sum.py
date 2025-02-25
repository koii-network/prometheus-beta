import pytest
from src.max_subarray_sum import kadanes_max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert kadanes_max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert kadanes_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with all negative numbers."""
    assert kadanes_max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    """Test with a single element."""
    assert kadanes_max_subarray_sum([42]) == 42

def test_all_zeros():
    """Test with all zero elements."""
    assert kadanes_max_subarray_sum([0, 0, 0, 0]) == 0

def test_large_numbers():
    """Test with large numbers."""
    assert kadanes_max_subarray_sum([1000000, -1000000, 1000000]) == 1000000

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        kadanes_max_subarray_sum([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        kadanes_max_subarray_sum("not a list")
        kadanes_max_subarray_sum(123)
        kadanes_max_subarray_sum(None)