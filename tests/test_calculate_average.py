import pytest
from src.calculate_average import calculate_average

def test_average_of_integers():
    """Test average calculation with integers"""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_average_of_floats():
    """Test average calculation with floating point numbers"""
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_average_of_mixed_numbers():
    """Test average calculation with mixed integer and float numbers"""
    assert calculate_average([1, 2.5, 3, 4.5]) == 2.75

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_non_numeric_list_raises_error():
    """Test that a list with non-numeric values raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_average([1, 2, 'three', 4])

def test_single_number():
    """Test average calculation with a single number"""
    assert calculate_average([42]) == 42.0