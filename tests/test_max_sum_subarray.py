import pytest
from src.max_sum_subarray import max_sum_subarray

def test_max_sum_subarray_positive_numbers():
    """Test with positive numbers"""
    assert max_sum_subarray([1, 2, 3, 4, 5]) == 15
    assert max_sum_subarray([5, 4, 3, 2, 1]) == 15

def test_max_sum_subarray_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sum_subarray([1, -1, 2, -3, 4, -5]) == 4

def test_max_sum_subarray_all_negative():
    """Test with all negative numbers"""
    assert max_sum_subarray([-1, -2, -3, -4, -5]) == -1
    assert max_sum_subarray([-5, -4, -3, -2, -1]) == -1

def test_max_sum_subarray_single_element():
    """Test with single element arrays"""
    assert max_sum_subarray([42]) == 42
    assert max_sum_subarray([-42]) == -42

def test_max_sum_subarray_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        max_sum_subarray("not a list")
    
    with pytest.raises(TypeError):
        max_sum_subarray(123)
    
    with pytest.raises(ValueError):
        max_sum_subarray([])