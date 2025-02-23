import pytest
from src.max_non_overlapping_subarray import max_non_overlapping_subarray_sum

def test_basic_positive_array():
    """Test with a basic array of positive integers."""
    assert max_non_overlapping_subarray_sum([1, 2, 3, 4, 5]) == 7

def test_array_with_negatives():
    """Test an array containing negative numbers."""
    assert max_non_overlapping_subarray_sum([-1, 2, -3, 4, 5]) == 7

def test_empty_array():
    """Test an empty array returns 0."""
    assert max_non_overlapping_subarray_sum([]) == 0

def test_single_element_array():
    """Test an array with a single element."""
    assert max_non_overlapping_subarray_sum([5]) == 0
    assert max_non_overlapping_subarray_sum([-5]) == 0

def test_all_negative_array():
    """Test an array with all negative numbers."""
    assert max_non_overlapping_subarray_sum([-1, -2, -3, -4, -5]) == 0

def test_mixed_array_1():
    """Test a more complex mixed array."""
    assert max_non_overlapping_subarray_sum([3, -1, 4, -1, 5, 9, -2, 6]) == 14

def test_invalid_input_type():
    """Test that a non-list input raises TypeError."""
    with pytest.raises(TypeError):
        max_non_overlapping_subarray_sum("not a list")

def test_invalid_list_elements():
    """Test that a list with non-integer elements raises ValueError."""
    with pytest.raises(ValueError):
        max_non_overlapping_subarray_sum([1, 2, "3", 4, 5])

def test_large_values():
    """Test with large integer values."""
    assert max_non_overlapping_subarray_sum([10000, -5000, 20000, -10000, 15000]) == 25000