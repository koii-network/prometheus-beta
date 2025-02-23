import pytest
import math
from src.closest_points import find_closest_points

def test_basic_closest_points():
    """Test finding closest points in simple scenario"""
    points_a = [(0, 0), (1, 1), (3, 3)]
    points_b = [(2, 2), (4, 4), (5, 5)]
    
    result = find_closest_points(points_a, points_b)
    assert result == ((1, 1), (2, 2))

def test_points_with_float_coordinates():
    """Test with floating point coordinates"""
    points_a = [(0.5, 0.5), (1.1, 1.1)]
    points_b = [(1.0, 1.0), (2.0, 2.0)]
    
    result = find_closest_points(points_a, points_b)
    
    # Check if result is as expected (either of the matching closest points)
    expected_pairs = [
        ((0.5, 0.5), (1.0, 1.0)),
        ((1.1, 1.1), (1.0, 1.0))
    ]
    assert result in expected_pairs

def test_empty_lists():
    """Test behavior with empty lists"""
    points_a = []
    points_b = [(1, 1), (2, 2)]
    
    result = find_closest_points(points_a, points_b)
    assert result is None
    
    points_a = [(1, 1), (2, 2)]
    points_b = []
    
    result = find_closest_points(points_a, points_b)
    assert result is None

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        find_closest_points("not a list", [(1, 1)])
    
    with pytest.raises(TypeError):
        find_closest_points([(1, 1)], "not a list")

def test_invalid_point_formats():
    """Test error handling for invalid point formats"""
    with pytest.raises(ValueError):
        find_closest_points([(1, 1, 1)], [(2, 2)])
    
    with pytest.raises(ValueError):
        find_closest_points([(1, 'a')], [(2, 2)])

def test_single_points_in_lists():
    """Test scenario with single points in each list"""
    points_a = [(0, 0)]
    points_b = [(3, 4)]
    
    result = find_closest_points(points_a, points_b)
    assert result == ((0, 0), (3, 4))

def test_multiple_closest_points():
    """Verify behavior when multiple point pairs have same distance"""
    points_a = [(1, 1), (2, 2)]
    points_b = [(1.5, 1.5), (2.5, 2.5)]
    
    result = find_closest_points(points_a, points_b)
    
    # Result should be one of these pairs with closest distance
    expected_pairs = [
        ((1, 1), (1.5, 1.5)),
        ((2, 2), (1.5, 1.5)),
        ((1, 1), (2.5, 2.5)),
        ((2, 2), (2.5, 2.5))
    ]
    assert result in expected_pairs