import pytest
import math
from src.circle_area import calculate_circle_area

def test_positive_radius():
    """Test area calculation for a positive radius"""
    radius = 5
    expected_area = math.pi * 5 ** 2
    assert calculate_circle_area(radius) == expected_area

def test_zero_radius():
    """Test area calculation for zero radius"""
    assert calculate_circle_area(0) == 0

def test_float_radius():
    """Test area calculation for float radius"""
    radius = 2.5
    expected_area = math.pi * 2.5 ** 2
    assert calculate_circle_area(radius) == expected_area

def test_negative_radius_raises_error():
    """Test that negative radius raises ValueError"""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        calculate_circle_area(-5)

def test_non_numeric_radius_raises_error():
    """Test that non-numeric radius raises TypeError"""
    with pytest.raises(TypeError, match="Radius must be a number"):
        calculate_circle_area("not a number")
    
    with pytest.raises(TypeError, match="Radius must be a number"):
        calculate_circle_area([1, 2, 3])