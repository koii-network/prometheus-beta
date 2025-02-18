import pytest
from src.variance import calculate_variance

def test_calculate_variance_normal_list():
    """Test variance calculation with a standard list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    expected_variance = 2.0  # (1.5)^2 = 2.0
    assert calculate_variance(numbers) == pytest.approx(2.0)

def test_calculate_variance_single_element():
    """Test variance calculation with a single-element list."""
    numbers = [42]
    assert calculate_variance(numbers) == 0.0

def test_calculate_variance_zero_values():
    """Test variance calculation with a list of zeros."""
    numbers = [0, 0, 0, 0]
    assert calculate_variance(numbers) == 0.0

def test_calculate_variance_mixed_numbers():
    """Test variance calculation with mixed positive and negative numbers."""
    numbers = [-2, 0, 2, 4, -4]
    expected_variance = 8.0  # Corrected expected variance
    assert calculate_variance(numbers) == pytest.approx(8.0)

def test_variance_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate variance of an empty list"):
        calculate_variance([])

def test_variance_non_numeric_list():
    """Test that a list with non-numeric values raises a TypeError."""
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        calculate_variance([1, 2, 'three', 4, 5])

def test_variance_float_precision():
    """Test variance calculation with floating point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5]
    expected_variance = 1.25  # Approximately
    assert calculate_variance(numbers) == pytest.approx(1.25)