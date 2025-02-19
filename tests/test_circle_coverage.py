import pytest
import math
from src.circle_coverage import Circle, minimum_circle_coverage, circles_overlap, calculate_distance

def test_empty_input():
    """Test handling of empty input list."""
    assert len(minimum_circle_coverage([])) == 0

def test_single_circle():
    """Test coverage when only one circle is present."""
    circle = Circle(0, 0, 5)
    coverage = minimum_circle_coverage([circle])
    assert len(coverage) == 1
    assert coverage[0] == circle

def test_non_overlapping_circles():
    """Test coverage of non-overlapping circles."""
    circles = [
        Circle(0, 0, 2),
        Circle(5, 5, 1),
        Circle(-3, -3, 1.5)
    ]
    coverage = minimum_circle_coverage(circles)
    assert len(coverage) == len(circles)

def test_overlapping_circles():
    """Test coverage of overlapping circles."""
    circles = [
        Circle(0, 0, 3),    # Large circle
        Circle(1, 1, 1),    # Smaller circle inside the first
        Circle(4, 4, 2)     # Another circle
    ]
    coverage = minimum_circle_coverage(circles)
    assert len(coverage) == 2  # Should cover with 2 circles

def test_extensive_overlap():
    """Test complex scenario with extensive overlap."""
    circles = [
        Circle(0, 0, 5),    # Large circle
        Circle(1, 1, 2),    # Smaller circle inside first
        Circle(6, 6, 3),    # Another circle
        Circle(7, 7, 1),    # Small circle
        Circle(-5, -5, 4)   # Distant circle
    ]
    coverage = minimum_circle_coverage(circles)
    assert len(coverage) <= len(circles)

def test_circles_overlap_detection():
    """Test circle overlap detection."""
    # Overlapping circles
    assert circles_overlap(Circle(0, 0, 3), Circle(1, 1, 2)) == True
    
    # Touching circles
    assert circles_overlap(Circle(0, 0, 3), Circle(6, 0, 3)) == True
    
    # Non-overlapping circles
    assert circles_overlap(Circle(0, 0, 1), Circle(5, 5, 1)) == False

def test_calculate_distance():
    """Test distance calculation between circle centers."""
    c1 = Circle(0, 0, 1)
    c2 = Circle(3, 4, 1)
    
    distance = calculate_distance(c1, c2)
    assert math.isclose(distance, 5, rel_tol=1e-9)
    
    c3 = Circle(1, 1, 2)
    c4 = Circle(4, 5, 3)
    
    distance = calculate_distance(c3, c4)
    assert math.isclose(distance, 5, rel_tol=1e-9)