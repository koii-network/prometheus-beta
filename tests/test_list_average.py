import pytest
from src.list_average import calculate_average

def test_calculate_average_basic():
    """Test basic average calculation."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_average_float():
    """Test average calculation with float values."""
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_calculate_average_mixed_types():
    """Test average calculation with mixed integer and float values."""
    assert calculate_average([1, 2.5, 3, 4.5]) == 2.75

def test_calculate_average_single_element():
    """Test average calculation with a single element."""
    assert calculate_average([42]) == 42.0

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_average("not a list")

def test_list_with_non_numeric_raises_error():
    """Test that a list with non-numeric values raises a TypeError."""
    with pytest.raises(TypeError, match="List must contain only numeric values"):
        calculate_average([1, 2, "three", 4])

def test_list_with_nested_list_raises_error():
    """Test that a list with nested lists raises a TypeError."""
    with pytest.raises(TypeError, match="List must contain only numeric values"):
        calculate_average([1, 2, [3], 4])