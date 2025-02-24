import pytest
from src.array_sum import calculate_array_sum

def test_sum_positive_integers():
    """Test summing positive integers."""
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_sum_negative_integers():
    """Test summing negative integers."""
    assert calculate_array_sum([-1, -2, -3]) == -6

def test_sum_mixed_numbers():
    """Test summing mixed positive and negative numbers."""
    assert calculate_array_sum([-1, 0, 1, 2.5]) == 2.5

def test_sum_single_element():
    """Test summing a single element list."""
    assert calculate_array_sum([42]) == 42

def test_sum_floating_point_numbers():
    """Test summing floating point numbers."""
    assert calculate_array_sum([1.5, 2.5, 3.0]) == 7.0

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate sum of an empty list"):
        calculate_array_sum([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_non_numeric_elements_raises_error():
    """Test that list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "three", 4])

def test_large_numbers():
    """Test summing large numbers."""
    large_nums = [10**6, 10**7, 10**8]
    assert calculate_array_sum(large_nums) == 1.11e8