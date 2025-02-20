import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_positive_array():
    """Test with a basic array of positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_array_with_negative_numbers():
    """Test with an array containing negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_single_element_array():
    """Test with a single element array"""
    assert max_subarray_sum([5]) == 5

def test_all_negative_numbers():
    """Test with an array of all negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_alternating_positive_negative():
    """Test with alternating positive and negative numbers"""
    assert max_subarray_sum([1, -1, 2, -3, 4, -5]) == 4

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")

def test_empty_list():
    """Test that ValueError is raised for an empty list"""
    with pytest.raises(ValueError):
        max_subarray_sum([])