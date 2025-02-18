import pytest
import math
from src.circle_area import calculate_circle_area

def test_circle_area_positive_radius():
    """Test circle area calculation with positive radii."""
    assert calculate_circle_area(1) == math.pi
    assert calculate_circle_area(0) == 0
    assert calculate_circle_area(2.5) == math.pi * (2.5 ** 2)

def test_circle_area_large_radius():
    """Test circle area calculation with larger radii."""
    assert calculate_circle_area(10) == math.pi * (10 ** 2)
    assert calculate_circle_area(100.5) == math.pi * (100.5 ** 2)

def test_circle_area_negative_radius():
    """Test that negative radius raises a ValueError."""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        calculate_circle_area(-1)
        calculate_circle_area(-5.5)