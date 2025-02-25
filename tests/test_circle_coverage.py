import pytest
import math
from src.circle_coverage import Circle, calculate_distance, do_circles_overlap, min_circle_coverage

def test_circle_creation():
    """Test Circle class initialization"""
    c = Circle(1.0, 2.0, 3.0)
    assert c.x == 1.0
    assert c.y == 2.0
    assert c.radius == 3.0

def test_calculate_distance():
    """Test distance calculation between circles"""
    c1 = Circle(0, 0, 1)
    c2 = Circle(3, 4, 1)
    distance = calculate_distance(c1, c2)
    assert math.isclose(distance, 5.0)

def test_circles_overlap():
    """Test circle overlap detection"""
    c1 = Circle(0, 0, 2)
    c2 = Circle(1, 1, 2)
    c3 = Circle(5, 5, 1)
    
    assert do_circles_overlap(c1, c2) == True
    assert do_circles_overlap(c1, c3) == False

def test_min_circle_coverage_single_circle():
    """Test minimum circle coverage with single circle"""
    c = Circle(1, 1, 2)
    result = min_circle_coverage([c])
    assert len(result) == 1
    assert result[0] == c

def test_min_circle_coverage_no_overlap():
    """Test circle coverage when no circles overlap"""
    c1 = Circle(0, 0, 1)
    c2 = Circle(5, 5, 1)
    c3 = Circle(10, 10, 1)
    
    result = min_circle_coverage([c1, c2, c3])
    assert len(result) == 3

def test_min_circle_coverage_with_overlap():
    """Test circle coverage with overlapping circles"""
    c1 = Circle(0, 0, 3)  # Large covering circle
    c2 = Circle(1, 1, 1)  # Smaller overlapping circle
    c3 = Circle(2, 2, 1)  # Another overlapping circle
    
    result = min_circle_coverage([c1, c2, c3])
    assert len(result) == 1
    assert result[0] == c1

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError"""
    with pytest.raises(ValueError):
        min_circle_coverage([])

def test_circle_coverage_complex_scenario():
    """Test a more complex scenario with multiple circles"""
    circles = [
        Circle(0, 0, 2),    # Center circle
        Circle(3, 3, 1),    # Overlapping circle
        Circle(1, 1, 1.5),  # Another overlapping circle
        Circle(6, 6, 1),    # Non-overlapping circle
    ]
    
    result = min_circle_coverage(circles)
    assert len(result) <= len(circles)  # Covering circles <= Input circles