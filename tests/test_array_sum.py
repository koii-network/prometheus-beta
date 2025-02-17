import pytest
from src.array_sum import calculate_array_sum

def test_sum_of_positive_integers():
    """Test sum of positive integers."""
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_sum_of_negative_integers():
    """Test sum of negative integers."""
    assert calculate_array_sum([-1, -2, -3, -4, -5]) == -15

def test_sum_of_mixed_numbers():
    """Test sum of mixed positive and negative numbers."""
    assert calculate_array_sum([-1, 2, -3, 4, -5]) == -3

def test_sum_of_floating_point_numbers():
    """Test sum of floating point numbers."""
    assert calculate_array_sum([1.5, 2.5, 3.0]) == 7.0

def test_sum_of_empty_array():
    """Test sum of an empty array."""
    assert calculate_array_sum([]) == 0

def test_input_not_list():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_non_numeric_elements():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "three", 4])