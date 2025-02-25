import pytest
from src.array_sum import sum_array

def test_sum_array_normal_case():
    """Test sum of a normal array of positive integers."""
    assert sum_array([1, 2, 3, 4, 5]) == 15

def test_sum_array_empty():
    """Test sum of an empty array."""
    assert sum_array([]) == 0

def test_sum_array_negative_numbers():
    """Test sum of array with negative numbers."""
    assert sum_array([-1, -2, -3]) == -6

def test_sum_array_mixed_numbers():
    """Test sum of array with mixed positive and negative numbers."""
    assert sum_array([-1, 0, 1]) == 0

def test_sum_array_single_element():
    """Test sum of an array with a single element."""
    assert sum_array([42]) == 42

def test_sum_array_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_array(123)

def test_sum_array_non_integer_elements():
    """Test that an array with non-integer elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_array([1, 2, '3', 4])