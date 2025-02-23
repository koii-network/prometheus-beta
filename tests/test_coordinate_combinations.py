import pytest
from src.coordinate_combinations import get_unique_coordinate_combinations

def test_basic_coordinate_combinations():
    """Test basic functionality with simple coordinate pairs."""
    coordinates = [(1, 2), (3, 4), (2, 1)]
    result = get_unique_coordinate_combinations(coordinates)
    assert result == [1, 2, 3, 4]

def test_duplicate_coordinates():
    """Test handling of duplicate coordinate values."""
    coordinates = [(1, 1), (2, 2), (1, 2), (2, 1)]
    result = get_unique_coordinate_combinations(coordinates)
    assert result == [1, 2]

def test_negative_coordinates():
    """Test handling of negative coordinate values."""
    coordinates = [(-1, 2), (3, -4), (0, 0)]
    result = get_unique_coordinate_combinations(coordinates)
    assert result == [-4, -1, 0, 2, 3]

def test_float_coordinates():
    """Test handling of floating-point coordinate values."""
    coordinates = [(1.5, 2.7), (3.2, 1.1), (2.5, 3.8)]
    result = get_unique_coordinate_combinations(coordinates)
    assert result == [1.1, 1.5, 2.5, 2.7, 3.2, 3.8]

def test_empty_list():
    """Test handling of an empty list."""
    coordinates = []
    result = get_unique_coordinate_combinations(coordinates)
    assert result == []

def test_invalid_input_not_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of coordinate pairs"):
        get_unique_coordinate_combinations("not a list")

def test_invalid_coordinate_pair():
    """Test that a ValueError is raised for invalid coordinate pairs."""
    with pytest.raises(ValueError, match="Invalid coordinate pair"):
        get_unique_coordinate_combinations([(1, 2), "invalid", (3, 4)])

def test_non_numeric_coordinates():
    """Test that a ValueError is raised for non-numeric coordinates."""
    with pytest.raises(ValueError, match="Coordinate values must be numeric"):
        get_unique_coordinate_combinations([(1, 'a'), (2, 3)])