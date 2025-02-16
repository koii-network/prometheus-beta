import pytest
import math
from src.standard_deviation import calculate_standard_deviation

def test_standard_deviation_basic():
    """Test standard deviation with a simple list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    expected = math.sqrt(sum((x - 3) ** 2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-9)

def test_standard_deviation_single_element():
    """Test standard deviation with a single element."""
    numbers = [42]
    assert calculate_standard_deviation(numbers) == 0.0

def test_standard_deviation_with_floats():
    """Test standard deviation with floating point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected = math.sqrt(sum((x - 3.5) ** 2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-9)

def test_standard_deviation_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate standard deviation of an empty list"):
        calculate_standard_deviation([])

def test_standard_deviation_non_numeric():
    """Test that a list with non-numeric values raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_standard_deviation([1, 2, 'three', 4, 5])

def test_standard_deviation_large_numbers():
    """Test standard deviation with large numbers."""
    numbers = [10000, 20000, 30000, 40000, 50000]
    expected = math.sqrt(sum((x - 30000) ** 2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-9)