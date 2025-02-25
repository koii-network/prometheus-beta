import pytest
import math
from src.closest_points import find_closest_points

def test_basic_case():
    """Test basic scenario with simple point lists"""
    list_a = [(0, 0), (1, 1)]
    list_b = [(2, 2), (3, 3)]
    result = find_closest_points(list_a, list_b)
    assert result == ((1, 1), (2, 2))

def test_same_points():
    """Test when closest points are at the same coordinates"""
    list_a = [(1, 1), (2, 2)]
    list_b = [(1, 1), (3, 3)]
    result = find_closest_points(list_a, list_b)
    assert result == ((1, 1), (1, 1))

def test_empty_lists():
    """Test behavior with empty lists"""
    assert find_closest_points([], [(1, 1)]) is None
    assert find_closest_points([(1, 1)], []) is None
    assert find_closest_points([], []) is None

def test_single_point_lists():
    """Test lists with single points"""
    list_a = [(0, 0)]
    list_b = [(1, 1)]
    result = find_closest_points(list_a, list_b)
    assert result == ((0, 0), (1, 1))

def test_multiple_equidistant_points():
    """Test scenario with multiple points at same distance"""
    list_a = [(0, 0), (1, 1)]
    list_b = [(2, 2), (3, 3)]
    result = find_closest_points(list_a, list_b)
    assert result == ((1, 1), (2, 2))

def test_negative_coordinates():
    """Test points with negative coordinates"""
    list_a = [(-1, -1), (-2, -2)]
    list_b = [(-3, -3), (0, 0)]
    result = find_closest_points(list_a, list_b)
    # Verify the points are the closest
    expected_distance = math.sqrt(1**2 + 1**2)
    actual_distance = math.sqrt((result[0][0] - result[1][0])**2 + 
                                 (result[0][1] - result[1][1])**2)
    assert math.isclose(actual_distance, expected_distance, rel_tol=1e-9)

def test_floating_point_coordinates():
    """Test points with floating point coordinates"""
    list_a = [(0.5, 0.5), (1.5, 1.5)]
    list_b = [(1.1, 1.1), (2.2, 2.2)]
    result = find_closest_points(list_a, list_b)
    assert result == ((1.5, 1.5), (1.1, 1.1))

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        find_closest_points("not a list", [(1, 1)])
    with pytest.raises(TypeError):
        find_closest_points([(1, 1)], "not a list")
    with pytest.raises(TypeError):
        find_closest_points([(1, "a")], [(1, 1)])

def test_invalid_point_format():
    """Test error handling for invalid point formats"""
    with pytest.raises(ValueError):
        find_closest_points([(1,)], [(1, 1)])
    with pytest.raises(ValueError):
        find_closest_points([(1, 1, 1)], [(1, 1)])