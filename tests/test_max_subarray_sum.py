import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_positive_array():
    """Test with a basic positive integer array"""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_positive_negative():
    """Test with mixed positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with all negative numbers, should return the largest number"""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element_array():
    """Test with a single element array"""
    assert max_subarray_sum([42]) == 42

def test_floating_point_numbers():
    """Test with floating point numbers"""
    assert max_subarray_sum([1.5, -2.5, 3.7, -1.2, 2.1]) == 4.1

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError):
        max_subarray_sum([])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")
    with pytest.raises(TypeError):
        max_subarray_sum(123)

def test_list_with_non_numeric_input_raises_error():
    """Test that a list with non-numeric elements raises a TypeError"""
    with pytest.raises(TypeError):
        max_subarray_sum([1, 2, "three", 4])
    with pytest.raises(TypeError):
        max_subarray_sum([1, 2, None, 4])