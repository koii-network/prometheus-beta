import pytest
from src.max_subarray import max_subarray_sum

def test_positive_numbers():
    """Test with array of positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative():
    """Test with all negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test with single element array"""
    assert max_subarray_sum([5]) == 5

def test_alternating_signs():
    """Test with alternating positive and negative numbers"""
    assert max_subarray_sum([1, -1, 2, -2, 3]) == 3

def test_zero_elements():
    """Test with zero-valued elements"""
    assert max_subarray_sum([0, 0, 0, 0]) == 0

def test_invalid_input_empty_list():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_invalid_input_type():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")
        max_subarray_sum(123)
        max_subarray_sum(None)