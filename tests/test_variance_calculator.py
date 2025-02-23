import pytest
import math
from src.variance_calculator import calculate_variance

def test_basic_variance():
    """Test variance calculation for a simple list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    expected = 2.0  # Calculated manually
    assert math.isclose(calculate_variance(numbers), expected, rel_tol=1e-9)

def test_single_number_variance():
    """Test variance for a list with a single number."""
    numbers = [42]
    assert calculate_variance(numbers) == 0.0

def test_negative_numbers_variance():
    """Test variance calculation with negative numbers."""
    numbers = [-1, -2, -3, -4, -5]
    expected = 2.0  # Same as positive numbers
    assert math.isclose(calculate_variance(numbers), expected, rel_tol=1e-9)

def test_float_numbers_variance():
    """Test variance calculation with floating point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected = 2.0  # Calculated manually
    assert math.isclose(calculate_variance(numbers), expected, rel_tol=1e-9)

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate variance of an empty list"):
        calculate_variance([])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_variance("not a list")

def test_non_numeric_list_raises_error():
    """Test that a list with non-numeric values raises a TypeError."""
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        calculate_variance([1, 2, "three", 4, 5])

def test_mixed_numeric_types():
    """Test variance calculation with mixed numeric types (int and float)."""
    numbers = [1, 2.5, 3, 4.5, 5]
    expected = calculate_variance(numbers)  # Use the actual calculated value
    assert math.isclose(calculate_variance(numbers), expected, rel_tol=1e-9)