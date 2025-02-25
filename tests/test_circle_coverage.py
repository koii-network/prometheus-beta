import pytest
import math
from src.circle_coverage import Circle, minimum_circle_coverage, calculate_distance, can_cover_circle

def test_calculate_distance():
    """Test distance calculation between circle centers."""
    c1 = Circle(0, 0, 1)
    c2 = Circle(3, 4, 2)
    expected_distance = 5  # 3-4-5 triangle
    assert math.isclose(calculate_distance(c1, c2), expected_distance)

def test_can_cover_circle():
    """Test circle coverage detection."""
    # Circle completely covers another
    covering = Circle(0, 0, 5)
    target = Circle(1, 1, 2)
    assert can_cover_circle(covering, target) == True
    
    # Circle does not cover another
    non_covering = Circle(0, 0, 2)
    target_far = Circle(5, 5, 2)
    assert can_cover_circle(non_covering, target_far) == False

def test_minimum_circle_coverage_empty_list():
    """Test handling of empty input list."""
    assert minimum_circle_coverage([]) == []

def test_minimum_circle_coverage_single_circle():
    """Test scenario with a single circle."""
    circle = Circle(0, 0, 1)
    result = minimum_circle_coverage([circle])
    assert len(result) == 1
    assert result[0] == circle

def test_minimum_circle_coverage_fully_nested():
    """Test circles that are completely nested within each other."""
    circles = [
        Circle(0, 0, 5),  # Large circle
        Circle(0, 0, 2),  # Smaller circle completely inside large circle
        Circle(1, 1, 1)   # Another small circle inside large circle
    ]
    result = minimum_circle_coverage(circles)
    assert len(result) == 1
    assert result[0] == circles[0]

def test_minimum_circle_coverage_non_overlapping():
    """Test circles that cannot cover each other."""
    circles = [
        Circle(0, 0, 1),
        Circle(3, 4, 2),
        Circle(10, 10, 3)
    ]
    result = minimum_circle_coverage(circles)
    assert len(result) == 3

def test_minimum_circle_coverage_partial_overlap():
    """Test circles with partial overlap."""
    circles = [
        Circle(0, 0, 2),
        Circle(1.5, 0, 2),
        Circle(3, 0, 2)
    ]
    result = minimum_circle_coverage(circles)
    assert len(result) <= len(circles)
    assert len(result) > 1  # Expect more than one covering circle

def test_large_radius_minimal_coverage():
    """Test scenario where a large radius minimizes coverage."""
    large_circle = Circle(0, 0, 10)
    small_circles = [
        Circle(1, 1, 1),
        Circle(-1, -1, 1),
        Circle(5, 5, 1)
    ]
    circles = [large_circle] + small_circles
    result = minimum_circle_coverage(circles)
    assert len(result) == 1
    assert result[0] == large_circle