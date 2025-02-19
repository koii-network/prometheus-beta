import pytest
import math
from src.circle_coverage import Circle, find_minimum_circle_coverage, calculate_distance, is_circle_covering

def test_calculate_distance():
    # Test distance calculation between circles
    circle1 = Circle(0, 0, 1)
    circle2 = Circle(3, 4, 2)
    expected_distance = 5  # sqrt(3^2 + 4^2)
    assert math.isclose(calculate_distance(circle1, circle2), expected_distance)

def test_is_circle_covering():
    # Test when a circle completely covers another
    covering = Circle(0, 0, 5)
    covered = Circle(1, 1, 2)
    assert is_circle_covering(covering, covered) == True

    # Test when a circle does not cover another
    not_covering = Circle(0, 0, 2)
    not_covered = Circle(3, 3, 2)
    assert is_circle_covering(not_covering, not_covered) == False

def test_find_minimum_circle_coverage_single_circle():
    # Test with a single circle
    circle = Circle(0, 0, 1)
    result = find_minimum_circle_coverage([circle])
    assert len(result) == 1
    assert result[0] == circle

def test_find_minimum_circle_coverage_multiple_circles():
    # Test with multiple circles requiring coverage
    circles = [
        Circle(0, 0, 1),    # Small circle
        Circle(2, 2, 3),    # Larger circle that can cover others
        Circle(5, 5, 1)     # Another small circle
    ]
    result = find_minimum_circle_coverage(circles)
    assert len(result) <= len(circles)  # Fewer or equal number of covering circles

def test_find_minimum_circle_coverage_overlapping():
    # Test circles that overlap and require minimal coverage
    circles = [
        Circle(0, 0, 2),    # Can potentially cover multiple
        Circle(1, 1, 1),    # Smaller circle
        Circle(3, 3, 1)     # Another small circle
    ]
    result = find_minimum_circle_coverage(circles)
    assert len(result) < len(circles)  # Fewer covering circles

def test_find_minimum_circle_coverage_empty_input():
    # Test that an empty input raises a ValueError
    with pytest.raises(ValueError, match="Input list of circles cannot be empty"):
        find_minimum_circle_coverage([])

def test_find_minimum_circle_coverage_edge_cases():
    # Test with circles at different positions and radii
    circles = [
        Circle(-10, -10, 1),
        Circle(10, 10, 2),
        Circle(0, 0, 5),
        Circle(100, 100, 1)
    ]
    result = find_minimum_circle_coverage(circles)
    assert len(result) > 0  # Should always return at least one circle