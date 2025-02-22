import pytest
import math
from src.closest_points import find_closest_points

def test_find_closest_points_basic():
    """Test finding closest points in simple scenario"""
    list_a = [(0, 0), (1, 1), (3, 3)]
    list_b = [(2, 2), (4, 4), (5, 5)]
    
    result = find_closest_points(list_a, list_b)
    
    assert result[0] == (1, 1)
    assert result[1] == (2, 2)
    assert math.isclose(result[2], math.sqrt(2), rel_tol=1e-9)

def test_find_closest_points_negative_coordinates():
    """Test with points having negative coordinates"""
    list_a = [(-1, -1), (-3, -3), (0, 0)]
    list_b = [(-2, -2), (-4, -4), (1, 1)]
    
    result = find_closest_points(list_a, list_b)
    
    assert result[0] == (-1, -1)
    assert result[1] == (-2, -2)
    assert math.isclose(result[2], math.sqrt(2), rel_tol=1e-9)

def test_find_closest_points_same_point():
    """Test when closest points have same coordinates"""
    list_a = [(1, 1), (2, 2), (3, 3)]
    list_b = [(1, 1), (4, 4), (5, 5)]
    
    result = find_closest_points(list_a, list_b)
    
    assert result[0] == (1, 1)
    assert result[1] == (1, 1)
    assert result[2] == 0

def test_find_closest_points_empty_list_error():
    """Test that an error is raised when either list is empty"""
    with pytest.raises(ValueError, match="Both input lists must be non-empty"):
        find_closest_points([], [(1, 1)])
    
    with pytest.raises(ValueError, match="Both input lists must be non-empty"):
        find_closest_points([(1, 1)], [])