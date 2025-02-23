import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with an array of mixed positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test with an array of all negative numbers."""
    assert max_subarray_sum([-1, -2, -3]) == -1

def test_single_element():
    """Test with a single element array."""
    assert max_subarray_sum([42]) == 42

def test_zero_element_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_invalid_input_type():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")

def test_large_numbers():
    """Test with large numbers."""
    assert max_subarray_sum([10**9, -10**9, 10**9]) == 10**9

def test_alternating_numbers():
    """Test with alternating positive and negative numbers."""
    assert max_subarray_sum([1, -1, 2, -2, 3]) == 3