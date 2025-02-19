import pytest
from src.max_subarray_sum import find_max_subarray

def test_positive_numbers():
    """Test with an array of positive numbers"""
    arr = [1, 2, 3, 4, 5]
    assert find_max_subarray(arr) == [1, 2, 3, 4, 5]

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert find_max_subarray(arr) == [4, -1, 2, 1]

def test_all_negative_numbers():
    """Test with all negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    assert find_max_subarray(arr) == [-1]

def test_single_element():
    """Test with a single element"""
    arr = [42]
    assert find_max_subarray(arr) == [42]

def test_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_subarray([])

def test_multiple_subarrays_with_same_max_sum():
    """Test case with multiple subarrays having the same max sum"""
    arr = [1, -1, 2, -1, 2]
    result = find_max_subarray(arr)
    assert result in [[2], [2, -1, 2]]