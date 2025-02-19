import pytest
from src.kadane_algorithm import max_subarray_sum

def test_max_subarray_sum_positive_numbers():
    """Test Kadane's algorithm with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_max_subarray_sum_mixed_numbers():
    """Test Kadane's algorithm with mixed positive and negative numbers."""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_sum_all_negative():
    """Test Kadane's algorithm with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_max_subarray_sum_single_element():
    """Test Kadane's algorithm with a single element."""
    assert max_subarray_sum([42]) == 42

def test_max_subarray_sum_invalid_input_empty():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_max_subarray_sum_invalid_input_type():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")
        max_subarray_sum(123)
        max_subarray_sum(None)