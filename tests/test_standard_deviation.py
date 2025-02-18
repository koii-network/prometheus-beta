import pytest
import math
from src.standard_deviation import calculate_standard_deviation

def test_standard_deviation_basic():
    """Test standard deviation for a basic list of numbers"""
    numbers = [1, 2, 3, 4, 5]
    expected = math.sqrt(sum((x - 3) ** 2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-9)

def test_standard_deviation_single_number():
    """Test standard deviation for a single number"""
    numbers = [10]
    assert calculate_standard_deviation(numbers) == 0

def test_standard_deviation_float_numbers():
    """Test standard deviation with floating point numbers"""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected = math.sqrt(sum((x - 3.5) ** 2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-9)

def test_standard_deviation_empty_list():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot calculate standard deviation of an empty list"):
        calculate_standard_deviation([])

def test_standard_deviation_non_numeric():
    """Test that a list with non-numeric elements raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_standard_deviation([1, 2, '3', 4, 5])

def test_standard_deviation_negative_numbers():
    """Test standard deviation with negative numbers"""
    numbers = [-1, -2, -3, -4, -5]
    expected = math.sqrt(sum((x + 3) ** 2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-9)