import pytest
from src.variance_calculator import calculate_variance

def test_variance_basic():
    """Test variance calculation for a basic list of numbers"""
    numbers = [1, 2, 3, 4, 5]
    expected = 2.0  # (1-3)^2 + (2-3)^2 + (3-3)^2 + (4-3)^2 + (5-3)^2 = 10/5 = 2.0
    assert calculate_variance(numbers) == pytest.approx(2.0)

def test_variance_single_element():
    """Test variance for a single-element list"""
    numbers = [42]
    assert calculate_variance(numbers) == 0.0

def test_variance_floating_point():
    """Test variance with floating-point numbers"""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected = 2.0
    assert calculate_variance(numbers) == pytest.approx(2.0)

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot calculate variance of an empty list"):
        calculate_variance([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_variance("not a list")

def test_non_numeric_list_raises_error():
    """Test that a list with non-numeric values raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_variance([1, 2, "three", 4, 5])

def test_variance_zero():
    """Test variance of a list with identical elements"""
    numbers = [7, 7, 7, 7, 7]
    assert calculate_variance(numbers) == 0.0