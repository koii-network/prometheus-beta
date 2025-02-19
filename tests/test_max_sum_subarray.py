import pytest
from src.max_sum_subarray import find_max_sum_subarray

def test_positive_numbers():
    """Test with an array of positive numbers"""
    assert find_max_sum_subarray([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers"""
    assert find_max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with all negative numbers"""
    assert find_max_sum_subarray([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    """Test with a single element"""
    assert find_max_sum_subarray([42]) == 42

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError):
        find_max_sum_subarray([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError):
        find_max_sum_subarray("not a list")

def test_max_sum_at_beginning():
    """Test when max sum is at the beginning of the array"""
    assert find_max_sum_subarray([10, -5, 7, -3]) == 10

def test_max_sum_at_end():
    """Test when max sum is at the end of the array"""
    assert find_max_sum_subarray([-2, -3, 4]) == 4

def test_max_sum_in_middle():
    """Test when max sum is in the middle of the array"""
    assert find_max_sum_subarray([-1, -2, 5, 6, -7, -3, 4]) == 11