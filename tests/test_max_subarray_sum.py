import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test max subarray sum with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test max subarray sum with mixed positive and negative numbers."""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test max subarray sum with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test max subarray sum with a single element."""
    assert max_subarray_sum([42]) == 42

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])