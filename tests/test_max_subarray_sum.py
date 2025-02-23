import pytest
from src.max_subarray_sum import max_non_overlapping_subarray_sum

def test_basic_positive_array():
    """Test with a basic positive integer array"""
    arr = [1, 2, 3, 4, 5]
    assert max_non_overlapping_subarray_sum(arr) == 9

def test_negative_numbers():
    """Test with an array containing negative numbers"""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_non_overlapping_subarray_sum(arr) == 6

def test_all_negative_numbers():
    """Test with an array of all negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    assert max_non_overlapping_subarray_sum(arr) == 0

def test_empty_array():
    """Test with an empty array"""
    arr = []
    assert max_non_overlapping_subarray_sum(arr) == 0

def test_single_element_array():
    """Test with a single element array"""
    arr = [42]
    assert max_non_overlapping_subarray_sum(arr) == 42

def test_mixed_numbers():
    """Test with a mixed array of positive and negative numbers"""
    arr = [3, -4, 2, 7, -3, 1, 4]
    assert max_non_overlapping_subarray_sum(arr) == 12

def test_invalid_input_type():
    """Test with an invalid input type"""
    with pytest.raises(ValueError, match="Input must be a list of integers"):
        max_non_overlapping_subarray_sum(123)
        max_non_overlapping_subarray_sum("string")
        max_non_overlapping_subarray_sum(None)