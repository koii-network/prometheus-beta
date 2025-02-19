import pytest
from src.max_subarray_sum import max_subarray_sum

def test_max_subarray_sum_positive_numbers():
    """Test with an array of all positive numbers."""
    arr = [1, 2, 3, 4, 5]
    assert max_subarray_sum(arr) == 15

def test_max_subarray_sum_mixed_numbers():
    """Test with an array containing positive and negative numbers."""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(arr) == 6

def test_max_subarray_sum_all_negative():
    """Test with an array of all negative numbers."""
    arr = [-1, -2, -3, -4, -5]
    assert max_subarray_sum(arr) == -1

def test_max_subarray_sum_single_element():
    """Test with a single element array."""
    arr = [42]
    assert max_subarray_sum(arr) == 42

def test_max_subarray_sum_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        max_subarray_sum([])