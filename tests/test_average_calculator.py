import pytest
from src.average_calculator import calculate_average

def test_calculate_average_basic():
    """Test basic average calculation."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_average_with_floats():
    """Test average calculation with floating point numbers."""
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_calculate_average_single_number():
    """Test average calculation with a single number."""
    assert calculate_average([42]) == 42.0

def test_calculate_average_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_calculate_average_non_numeric():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_average([1, 2, '3', 4])

def test_calculate_average_mixed_numeric_types():
    """Test average calculation with mixed numeric types (int and float)."""
    assert calculate_average([1, 2.5, 3, 4.5]) == 2.75