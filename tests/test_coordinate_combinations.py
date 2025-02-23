import pytest
from src.coordinate_combinations import unique_coordinate_combinations

def test_basic_coordinate_combinations():
    """Test basic functionality with simple coordinate pairs"""
    coordinates = [(1, 2), (3, 4), (1, 5)]
    result = unique_coordinate_combinations(coordinates)
    assert result == [1, 2, 3, 4, 5]

def test_duplicate_coordinates():
    """Test handling of duplicate coordinates"""
    coordinates = [(1, 1), (1, 1), (2, 2), (2, 2)]
    result = unique_coordinate_combinations(coordinates)
    assert result == [1, 2]

def test_mixed_value_types():
    """Test coordinates with mixed int and float values"""
    coordinates = [(1.5, 2), (3, 4.5), (1.5, 5)]
    result = unique_coordinate_combinations(coordinates)
    assert result == [1.5, 2, 3, 4.5, 5]

def test_empty_list():
    """Test handling of an empty list"""
    coordinates = []
    result = unique_coordinate_combinations(coordinates)
    assert result == []

def test_invalid_input_type():
    """Test raising TypeError for invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list of coordinate pairs"):
        unique_coordinate_combinations("not a list")

def test_invalid_coordinate_type():
    """Test raising ValueError for invalid coordinate types"""
    with pytest.raises(ValueError, match="Each coordinate must be a tuple of \\(x, y\\)"):
        unique_coordinate_combinations([(1, 2), "invalid"])

def test_non_numeric_coordinates():
    """Test raising ValueError for non-numeric coordinates"""
    with pytest.raises(ValueError, match="Coordinates must be numeric values"):
        unique_coordinate_combinations([(1, "2"), (3, 4)])

def test_nested_coordinates():
    """Test coordinates with various numeric values"""
    coordinates = [(10, 20), (-5, 15), (0, 0)]
    result = unique_coordinate_combinations(coordinates)
    assert result == [-5, 0, 10, 15, 20]