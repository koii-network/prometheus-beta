import pytest
import math
from src.closest_points import find_closest_points

def test_find_closest_points_basic():
    """Test basic functionality with simple point lists."""
    A = [(0, 0), (1, 1), (3, 4)]
    B = [(2, 2), (5, 5), (0, 5)]
    
    closest_a, closest_b, distance = find_closest_points(A, B)
    
    # Expected result is points close to each other
    assert closest_a == (1, 1)
    assert closest_b == (2, 2)
    assert math.isclose(distance, math.sqrt(2), rel_tol=1e-9)

def test_find_closest_points_identical_coordinates():
    """Test when some points have identical coordinates."""
    A = [(0, 0), (1, 1), (1, 1)]
    B = [(2, 2), (1, 1), (5, 5)]
    
    closest_a, closest_b, distance = find_closest_points(A, B)
    
    assert closest_a == (1, 1)
    assert closest_b == (1, 1)
    assert distance == 0

def test_find_closest_points_large_lists():
    """Test with larger point lists."""
    A = [(i, i) for i in range(10)]
    B = [(i+0.5, i+0.5) for i in range(10)]
    
    closest_a, closest_b, distance = find_closest_points(A, B)
    
    assert math.isclose(distance, math.sqrt(0.5**2 + 0.5**2), rel_tol=1e-9)

def test_find_closest_points_empty_list_error():
    """Test that an error is raised when either list is empty."""
    A = [(0, 0), (1, 1)]
    B = []
    
    with pytest.raises(ValueError, match="Both input lists must contain at least one point"):
        find_closest_points(A, B)
    
    with pytest.raises(ValueError, match="Both input lists must contain at least one point"):
        find_closest_points([], B)

def test_find_closest_points_negative_coordinates():
    """Test with negative coordinate points."""
    A = [(-1, -1), (-3, -4), (0, 0)]
    B = [(-2, -2), (5, 5), (1, 1)]
    
    closest_a, closest_b, distance = find_closest_points(A, B)
    
    # Verify the result is mathematically correct
    assert math.isclose(distance, math.sqrt(2), rel_tol=1e-9)
    assert (closest_a, closest_b) in [((-1, -1), (-2, -2)), ((-2, -2), (-1, -1))]