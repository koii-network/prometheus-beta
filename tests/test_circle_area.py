import pytest
import math
from src.circle_area import calculate_circle_area

def test_circle_area_zero_radius():
    """Test area calculation for zero radius."""
    assert calculate_circle_area(0) == 0

def test_circle_area_positive_radius():
    """Test area calculation for various positive radii."""
    assert math.isclose(calculate_circle_area(1), math.pi)
    assert math.isclose(calculate_circle_area(2), 4 * math.pi)
    assert math.isclose(calculate_circle_area(3.5), 3.5 * 3.5 * math.pi)

def test_circle_area_negative_radius():
    """Test that negative radius raises a ValueError."""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        calculate_circle_area(-1)

def test_circle_area_type_error():
    """Test that non-numeric radii raise a TypeError."""
    with pytest.raises(TypeError):
        calculate_circle_area("not a number")
    with pytest.raises(TypeError):
        calculate_circle_area(None)