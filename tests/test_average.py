import pytest
from src.average import calculate_average

def test_calculate_average_basic():
    """Test basic average calculation."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([10, 20, 30]) == 20

def test_calculate_average_float():
    """Test average calculation with floating point numbers."""
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_calculate_average_single_element():
    """Test average calculation with a single element."""
    assert calculate_average([42]) == 42

def test_calculate_average_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_calculate_average_non_numeric():
    """Test that non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_average([1, 2, '3', 4])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_average([1, 2, None, 4])