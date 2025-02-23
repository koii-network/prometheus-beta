import pytest
from src.max_subarray import max_subarray_sum

def test_basic_positive_array():
    """Test a basic array with mixed positive and negative numbers."""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_positive_numbers():
    """Test an array with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_single_element_array():
    """Test an array with a single element."""
    assert max_subarray_sum([42]) == 42

def test_all_negative_numbers():
    """Test an array with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_mixed_large_numbers():
    """Test an array with large positive and negative numbers."""
    assert max_subarray_sum([10, -5, 7, -3, 15, -2, 8, -1]) == 30

def test_input_type_error():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")

def test_empty_list_error():
    """Test that a ValueError is raised for an empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])