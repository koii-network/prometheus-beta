import pytest
from src.circle_coverage import Circle, find_minimum_circle_coverage, circles_overlap, calculate_distance

def test_empty_circle_list():
    """Test that an empty list returns an empty list."""
    assert find_minimum_circle_coverage([]) == []

def test_single_circle():
    """Test that a single circle returns itself."""
    circle = Circle(0, 0, 5)
    result = find_minimum_circle_coverage([circle])
    assert len(result) == 1
    assert result[0] == circle

def test_no_overlap_circles():
    """Test circles that do not overlap."""
    circles = [
        Circle(0, 0, 3),
        Circle(5, 5, 2),
        Circle(-3, -3, 1)
    ]
    result = find_minimum_circle_coverage(circles)
    assert len(result) == 3

def test_overlapping_circles():
    """Test scenario with partially overlapping circles."""
    circles = [
        Circle(0, 0, 5),
        Circle(1, 1, 4),
        Circle(2, 2, 3)
    ]
    result = find_minimum_circle_coverage(circles)
    assert len(result) == 1
    assert result[0].radius == 5

def test_calculate_distance():
    """Test distance calculation between circles."""
    circle1 = Circle(0, 0, 1)
    circle2 = Circle(3, 4, 1)
    distance = calculate_distance(circle1, circle2)
    assert round(distance, 2) == 5

def test_circles_overlap():
    """Test circle overlap detection."""
    circle1 = Circle(0, 0, 3)
    circle2 = Circle(2, 0, 2)
    circle3 = Circle(10, 10, 1)
    
    assert circles_overlap(circle1, circle2) == True
    assert circles_overlap(circle1, circle3) == False