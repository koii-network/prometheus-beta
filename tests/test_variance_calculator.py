import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from variance_calculator import calculate_variance

def test_calculate_variance_basic():
    """Test variance calculation for a simple list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    expected_variance = 2.0  # (1-3)^2 + (2-3)^2 + (3-3)^2 + (4-3)^2 + (5-3)^2 = 4 / 5 = 2.0
    assert calculate_variance(numbers) == pytest.approx(expected_variance)

def test_calculate_variance_floats():
    """Test variance calculation with floating-point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected_variance = 2.0
    assert calculate_variance(numbers) == pytest.approx(expected_variance)

def test_calculate_variance_single_element():
    """Test variance calculation with a single element."""
    numbers = [42]
    assert calculate_variance(numbers) == 0.0

def test_calculate_variance_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate variance of an empty list"):
        calculate_variance([])

def test_calculate_variance_invalid_input_type():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_variance("not a list")

def test_calculate_variance_non_numeric_elements():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_variance([1, 2, "three", 4, 5])

def test_calculate_variance_mixed_numerics():
    """Test variance calculation with mixed integer and float types."""
    numbers = [1, 2.5, 3, 4.5, 5]
    expected_variance = 2.06  # Actual calculated variance with mixed types
    assert calculate_variance(numbers) == pytest.approx(expected_variance)