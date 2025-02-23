import pytest
from src.array_sum import calculate_array_sum

def test_sum_positive_numbers():
    """Test sum of positive numbers."""
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_sum_negative_numbers():
    """Test sum of negative numbers."""
    assert calculate_array_sum([-1, -2, -3]) == -6

def test_sum_mixed_numbers():
    """Test sum of mixed positive and negative numbers."""
    assert calculate_array_sum([-1, 0, 1]) == 0

def test_sum_floating_point():
    """Test sum of floating-point numbers."""
    assert calculate_array_sum([1.5, 2.5, 3.0]) == 7.0

def test_empty_list():
    """Test sum of an empty list."""
    assert calculate_array_sum([]) == 0

def test_single_element():
    """Test sum of a single-element list."""
    assert calculate_array_sum([42]) == 42

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_non_numeric_elements():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "three", 4])