import pytest
from src.coordinate_combinations import get_unique_coordinate_combinations

def test_basic_coordinate_combinations():
    """Test basic functionality with simple coordinate pairs"""
    coordinates = [(1, 2), (3, 4), (1, 4), (3, 2)]
    expected = [(1, 2), (1, 4), (3, 2), (3, 4)]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_duplicate_coordinates():
    """Test handling of duplicate coordinates"""
    coordinates = [(1, 2), (1, 2), (3, 4), (3, 4)]
    expected = [(1, 2), (1, 4), (3, 2), (3, 4)]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_single_coordinate():
    """Test a list with a single coordinate"""
    coordinates = [(5, 5)]
    expected = [(5, 5)]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_invalid_input_not_list():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of coordinate pairs"):
        get_unique_coordinate_combinations("not a list")

def test_invalid_coordinate_pairs():
    """Test that a TypeError is raised for invalid coordinate pairs"""
    with pytest.raises(TypeError, match="Each coordinate must be a pair of values"):
        get_unique_coordinate_combinations([(1, 2), (3), (4, 5)])

def test_empty_list():
    """Test behavior with an empty list"""
    assert get_unique_coordinate_combinations([]) == []