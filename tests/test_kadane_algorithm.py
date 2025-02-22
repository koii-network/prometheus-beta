import pytest
from src.kadane_algorithm import max_subarray_sum

def test_max_subarray_sum_positive_numbers():
    """Test with an array of positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4]) == 10
    assert max_subarray_sum([5, -2, 3, 4]) == 10

def test_max_subarray_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([-1, 2, -3, 4, -5]) == 4

def test_max_subarray_sum_all_negative():
    """Test with all negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_max_subarray_sum_single_element():
    """Test with a single element array"""
    assert max_subarray_sum([42]) == 42
    assert max_subarray_sum([-10]) == -10

def test_max_subarray_sum_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")
    
    with pytest.raises(ValueError):
        max_subarray_sum([])

def test_max_subarray_sum_zero_sum():
    """Test array with zero sum"""
    assert max_subarray_sum([0, 0, 0]) == 0
    assert max_subarray_sum([-1, 0, 1]) == 1