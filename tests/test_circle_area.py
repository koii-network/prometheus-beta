import pytest
import math
from src.circle_area import calculate_circle_area

def test_circle_area_positive_radius():
    """Test area calculation for positive radii."""
    assert math.isclose(calculate_circle_area(1), math.pi)
    assert math.isclose(calculate_circle_area(2), 4 * math.pi)
    assert math.isclose(calculate_circle_area(0), 0)

def test_circle_area_large_radius():
    """Test area calculation for large radii."""
    assert math.isclose(calculate_circle_area(10), 100 * math.pi)

def test_circle_area_zero_radius():
    """Test that a zero radius returns zero area."""
    assert calculate_circle_area(0) == 0

def test_circle_area_negative_radius():
    """Test that a negative radius raises a ValueError."""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        calculate_circle_area(-1)
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        calculate_circle_area(-100)