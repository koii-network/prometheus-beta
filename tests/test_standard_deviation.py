import pytest
import math
from src.standard_deviation import calculate_standard_deviation

def test_standard_deviation_basic():
    """Test standard deviation for a simple list of numbers."""
    numbers = [2, 4, 4, 4, 5, 5, 7, 9]
    expected = math.sqrt(sum((x - 5)**2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-10)

def test_standard_deviation_single_element():
    """Test standard deviation for a single-element list."""
    numbers = [5]
    assert calculate_standard_deviation(numbers) == 0.0

def test_standard_deviation_zero_values():
    """Test standard deviation for a list of zeros."""
    numbers = [0, 0, 0, 0]
    assert calculate_standard_deviation(numbers) == 0.0

def test_standard_deviation_floating_point():
    """Test standard deviation with floating-point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5]
    expected = math.sqrt(sum((x - 3.0)**2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-10)

def test_standard_deviation_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate standard deviation of an empty list"):
        calculate_standard_deviation([])

def test_standard_deviation_non_numeric():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_standard_deviation(['a', 'b', 'c'])
    
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_standard_deviation([1, 2, '3', 4])

def test_standard_deviation_mixed_numeric_types():
    """Test that the function works with mixed numeric types."""
    numbers = [1, 2, 3, 4, 5]
    expected = math.sqrt(sum((x - 3)**2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-10)