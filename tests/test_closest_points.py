import pytest
import math
from src.closest_points import find_closest_points

def test_basic_case():
    """Test a simple case with expected minimum distance."""
    A = [(0, 0), (1, 1), (3, 3)]
    B = [(2, 2), (4, 4), (5, 5)]
    
    closest_a, closest_b, distance = find_closest_points(A, B)
    
    assert math.isclose(distance, math.sqrt(2), rel_tol=1e-9)
    assert (closest_a, closest_b) in [
        ((1, 1), (2, 2)),
        ((3, 3), (2, 2))
    ]

def test_same_point_lists():
    """Test when both lists have the same points."""
    points = [(0, 0), (1, 1), (2, 2)]
    
    closest_a, closest_b, distance = find_closest_points(points, points)
    
    assert math.isclose(distance, math.sqrt(2), rel_tol=1e-9)
    assert (closest_a, closest_b) in [
        ((0, 0), (1, 1)),
        ((1, 1), (2, 2)),
        ((0, 0), (2, 2))
    ]

def test_large_coordinates():
    """Test with large coordinate values."""
    A = [(1000, 2000), (3000, 4000)]
    B = [(1500, 2500), (3500, 4500)]
    
    closest_a, closest_b, distance = find_closest_points(A, B)
    
    expected_distance = math.sqrt((1000 - 1500)**2 + (2000 - 2500)**2)
    assert math.isclose(distance, expected_distance, rel_tol=1e-9)

def test_floating_point_coordinates():
    """Test with floating-point coordinate values."""
    A = [(0.1, 0.2), (1.5, 2.7)]
    B = [(0.3, 0.4), (1.7, 2.9)]
    
    closest_a, closest_b, distance = find_closest_points(A, B)
    assert len(A) > 0 and len(B) > 0  # Ensure non-emptiness
    assert distance is not None

def test_empty_list_raises_error():
    """Test that empty lists raise a ValueError."""
    with pytest.raises(ValueError):
        find_closest_points([], [(1, 1)])
    
    with pytest.raises(ValueError):
        find_closest_points([(1, 1)], [])