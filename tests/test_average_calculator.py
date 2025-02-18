import pytest
from src.average_calculator import calculate_average

def test_average_basic():
    """Test calculating average of a basic list of numbers."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3

def test_average_with_floats():
    """Test calculating average with floating point numbers."""
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_average_single_number():
    """Test calculating average with a single number."""
    assert calculate_average([42]) == 42

def test_average_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_average_non_numeric():
    """Test that non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_average([1, 2, "three", 4])

def test_average_mixed_types():
    """Test handling of mixed numeric types."""
    assert calculate_average([1, 2, 3.0, 4]) == 2.5