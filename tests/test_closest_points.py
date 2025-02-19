import math
import pytest
from src.closest_points import find_closest_points

def test_basic_find_closest_points():
    """Test finding closest points between two lists of points."""
    list_a = [(0, 0), (1, 1), (2, 2)]
    list_b = [(3, 3), (4, 4), (0.5, 0.5)]
    
    closest_a, closest_b, distance = find_closest_points(list_a, list_b)
    
    # Point (0.5, 0.5) from list_b is closest to (1, 1) from list_a
    assert closest_a == (1, 1)
    assert closest_b == (0.5, 0.5)
    assert math.isclose(distance, math.sqrt(0.5**2 + 0.5**2), rel_tol=1e-9)

def test_floating_point_points():
    """Test with floating point coordinates."""
    list_a = [(0.1, 0.1), (1.5, 2.5), (3.3, 4.4)]
    list_b = [(0.2, 0.2), (5.5, 6.6), (2.2, 3.3)]
    
    closest_a, closest_b, distance = find_closest_points(list_a, list_b)
    
    assert closest_a is not None
    assert closest_b is not None
    assert distance >= 0

def test_empty_list_raises_error():
    """Test that empty lists raise a ValueError."""
    with pytest.raises(ValueError, match="Both input lists must contain at least one point"):
        find_closest_points([], [(1, 1)])
    
    with pytest.raises(ValueError, match="Both input lists must contain at least one point"):
        find_closest_points([(1, 1)], [])

def test_single_point_lists():
    """Test behavior with single point in each list."""
    list_a = [(0, 0)]
    list_b = [(3, 4)]
    
    closest_a, closest_b, distance = find_closest_points(list_a, list_b)
    
    assert closest_a == (0, 0)
    assert closest_b == (3, 4)
    assert math.isclose(distance, 5.0, rel_tol=1e-9)  # sqrt(3^2 + 4^2) = 5

def test_identical_points():
    """Test case with some identical points."""
    list_a = [(1, 1), (2, 2), (3, 3)]
    list_b = [(1, 1), (4, 4), (5, 5)]
    
    closest_a, closest_b, distance = find_closest_points(list_a, list_b)
    
    assert (closest_a, closest_b) == ((1, 1), (1, 1))
    assert distance == 0.0