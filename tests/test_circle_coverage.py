import pytest
import math
from src.circle_coverage import Circle, find_minimum_circle_coverage, calculate_distance, circles_overlap

def test_calculate_distance():
    circle1 = Circle(0, 0, 1)
    circle2 = Circle(3, 4, 1)
    assert math.isclose(calculate_distance(circle1, circle2), 5)

def test_circles_overlap():
    # Overlapping circles
    circle1 = Circle(0, 0, 2)
    circle2 = Circle(1, 1, 2)
    assert circles_overlap(circle1, circle2)

    # Non-overlapping circles
    circle3 = Circle(0, 0, 1)
    circle4 = Circle(5, 5, 1)
    assert not circles_overlap(circle3, circle4)

def test_find_minimum_circle_coverage_empty_list():
    assert find_minimum_circle_coverage([]) == []

def test_find_minimum_circle_coverage_single_circle():
    circle = Circle(0, 0, 1)
    result = find_minimum_circle_coverage([circle])
    assert len(result) == 1
    assert result[0] == circle

def test_find_minimum_circle_coverage_multiple_overlapping_circles():
    # Create circles that require minimal coverage
    circle1 = Circle(0, 0, 3)
    circle2 = Circle(2, 2, 2)
    circle3 = Circle(5, 5, 1)
    circle4 = Circle(0, 5, 2)

    result = find_minimum_circle_coverage([circle1, circle2, circle3, circle4])
    
    # Verify minimum number of covering circles
    assert len(result) <= len([circle1, circle2, circle3, circle4])
    
    # Verify all input circles are covered
    def is_covered(input_circle, coverage_circles):
        return any(circles_overlap(input_circle, coverage_circle) for coverage_circle in coverage_circles)
    
    for input_circle in [circle1, circle2, circle3, circle4]:
        assert is_covered(input_circle, result), f"Circle {input_circle} not covered"