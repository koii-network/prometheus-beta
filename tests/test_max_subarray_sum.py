import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with all positive numbers"""
    arr = [1, 2, 3, 4, 5]
    assert max_subarray_sum(arr) == 15

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(arr) == 6

def test_all_negative_numbers():
    """Test with all negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    assert max_subarray_sum(arr) == -1

def test_single_element():
    """Test with a single element list"""
    arr = [42]
    assert max_subarray_sum(arr) == 42

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")
        max_subarray_sum(123)
        max_subarray_sum(None)