import pytest
import math
from src.circle_area import calculate_circle_area

def test_circle_area_positive_radius():
    """Test area calculation for a positive radius."""
    radius = 5
    expected_area = math.pi * radius ** 2
    assert calculate_circle_area(radius) == expected_area

def test_circle_area_zero_radius():
    """Test area calculation for zero radius."""
    assert calculate_circle_area(0) == 0

def test_circle_area_negative_radius():
    """Test that a negative radius raises a ValueError."""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        calculate_circle_area(-1)

def test_circle_area_floating_point():
    """Test area calculation with floating point radius."""
    radius = 2.5
    expected_area = math.pi * radius ** 2
    assert calculate_circle_area(radius) == expected_area