import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with all negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test with a single element"""
    assert max_subarray_sum([42]) == 42

def test_zero_element():
    """Test with zero"""
    assert max_subarray_sum([0]) == 0

def test_alternating_numbers():
    """Test with alternating positive and negative numbers"""
    assert max_subarray_sum([-1, 1, -1, 1]) == 1

def test_large_numbers():
    """Test with larger numbers"""
    assert max_subarray_sum([1000000, -1, 1000000]) == 1999999

def test_invalid_input_type():
    """Test with invalid input type"""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")

def test_empty_list():
    """Test with empty list"""
    with pytest.raises(ValueError):
        max_subarray_sum([])