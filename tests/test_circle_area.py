import pytest
import math
from src.circle_area import calculate_circle_area

def test_positive_radius():
    """Test area calculation for positive radii."""
    # Test a few known values
    assert math.isclose(calculate_circle_area(1), math.pi, rel_tol=1e-10)
    assert math.isclose(calculate_circle_area(0), 0, rel_tol=1e-10)
    assert math.isclose(calculate_circle_area(2), 4 * math.pi, rel_tol=1e-10)

def test_zero_radius():
    """Test area calculation for zero radius."""
    assert calculate_circle_area(0) == 0

def test_negative_radius():
    """Test that negative radius raises a ValueError."""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        calculate_circle_area(-1)

def test_invalid_input_type():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Radius must be a number"):
        calculate_circle_area("not a number")
    
    with pytest.raises(TypeError, match="Radius must be a number"):
        calculate_circle_area([1, 2, 3])
    
    with pytest.raises(TypeError, match="Radius must be a number"):
        calculate_circle_area(None)

def test_floating_point_radius():
    """Test area calculation with floating point radii."""
    assert math.isclose(calculate_circle_area(0.5), 0.25 * math.pi, rel_tol=1e-10)
    assert math.isclose(calculate_circle_area(3.14), math.pi * (3.14 ** 2), rel_tol=1e-10)