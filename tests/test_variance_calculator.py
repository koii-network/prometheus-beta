import pytest
from src.variance_calculator import calculate_variance

def test_normal_variance():
    """Test variance calculation for a normal list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    assert round(calculate_variance(numbers), 4) == 2.0000

def test_single_number():
    """Test variance for a single number."""
    numbers = [42]
    assert calculate_variance(numbers) == 0.0

def test_same_numbers():
    """Test variance for a list with identical numbers."""
    numbers = [7, 7, 7, 7]
    assert calculate_variance(numbers) == 0.0

def test_floating_point_numbers():
    """Test variance with floating point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5]
    assert round(calculate_variance(numbers), 4) == 1.2500

def test_mixed_integer_float():
    """Test variance with mixed integer and float numbers."""
    numbers = [1, 2.5, 3, 4.5, 5]
    assert round(calculate_variance(numbers), 4) == 2.0600

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate variance of an empty list"):
        calculate_variance([])

def test_non_numeric_list_raises_error():
    """Test that a list with non-numeric values raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_variance([1, 2, 'three', 4])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_variance("not a list")
        calculate_variance(123)
        calculate_variance(None)