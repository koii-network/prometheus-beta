import pytest
from src.list_average import calculate_average

def test_calculate_average_basic():
    """Test basic average calculation."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_average_floats():
    """Test average calculation with floating-point numbers."""
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_calculate_average_single_element():
    """Test average calculation with a single element."""
    assert calculate_average([42]) == 42.0

def test_calculate_average_negative_numbers():
    """Test average calculation with negative numbers."""
    assert calculate_average([-1, -2, -3]) == -2.0

def test_calculate_average_mixed_numbers():
    """Test average calculation with mixed positive and negative numbers."""
    assert calculate_average([-1, 0, 1]) == 0.0

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_average("not a list")

def test_non_numeric_list_raises_error():
    """Test that a list with non-numeric values raises a TypeError."""
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        calculate_average([1, 2, "three"])