import pytest
import math
from src.closest_points import find_closest_points

def test_find_closest_points_basic():
    """Test basic scenario with clear closest points"""
    A = [(0, 0), (1, 1), (3, 3)]
    B = [(2, 2), (4, 4), (5, 5)]
    
    closest_a, closest_b, distance = find_closest_points(A, B)
    
    assert closest_a == (1, 1)
    assert closest_b == (2, 2)
    assert math.isclose(distance, math.sqrt(2), rel_tol=1e-9)

def test_find_closest_points_equal_points():
    """Test when points are exactly the same"""
    A = [(1, 1), (2, 2), (3, 3)]
    B = [(2, 2), (4, 4), (5, 5)]
    
    closest_a, closest_b, distance = find_closest_points(A, B)
    
    assert closest_a == (2, 2)
    assert closest_b == (2, 2)
    assert distance == 0

def test_find_closest_points_large_sets():
    """Test with larger sets of points"""
    A = [(0, 0), (10, 10), (20, 20), (30, 30)]
    B = [(5, 5), (15, 15), (25, 25), (35, 35)]
    
    closest_a, closest_b, distance = find_closest_points(A, B)
    
    assert math.isclose(distance, math.sqrt(50), rel_tol=1e-9)
    assert closest_a == (10, 10)
    assert closest_b == (15, 15)

def test_find_closest_points_empty_lists():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Both input lists must be non-empty"):
        find_closest_points([], [(1, 1)])
    
    with pytest.raises(ValueError, match="Both input lists must be non-empty"):
        find_closest_points([(1, 1)], [])