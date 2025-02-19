import pytest
from src.max_sum_subarray import max_sum_subarray

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert max_sum_subarray([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with an array of mixed positive and negative numbers."""
    assert max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with an array of all negative numbers."""
    assert max_sum_subarray([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    """Test with a single element array."""
    assert max_sum_subarray([42]) == 42

def test_type_error():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        max_sum_subarray("not a list")

def test_empty_list():
    """Test that ValueError is raised for an empty list."""
    with pytest.raises(ValueError):
        max_sum_subarray([])