import pytest
from src.unique_coordinate_combinations import get_unique_coordinate_combinations

def test_basic_coordinate_combinations():
    coords = [(1, 2), (3, 4), (1, 4), (3, 2)]
    result = get_unique_coordinate_combinations(coords)
    expected = [(1, 2), (1, 4), (3, 2), (3, 4)]
    assert result == expected

def test_duplicate_coordinates():
    coords = [(1, 1), (1, 1), (2, 2), (2, 2)]
    result = get_unique_coordinate_combinations(coords)
    expected = [(1, 1), (1, 2), (2, 1), (2, 2)]
    assert result == expected

def test_single_coordinate():
    coords = [(5, 5)]
    result = get_unique_coordinate_combinations(coords)
    expected = [(5, 5)]
    assert result == expected

def test_floating_point_coordinates():
    coords = [(1.5, 2.5), (1.5, 3.5), (2.5, 2.5)]
    result = get_unique_coordinate_combinations(coords)
    expected = [(1.5, 2.5), (1.5, 3.5), (2.5, 2.5)]
    assert result == expected

def test_empty_list():
    coords = []
    result = get_unique_coordinate_combinations(coords)
    assert result == []

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list of coordinate pairs"):
        get_unique_coordinate_combinations("not a list")

def test_invalid_coordinate_type():
    with pytest.raises(TypeError, match="Each coordinate must be a tuple of two numeric values"):
        get_unique_coordinate_combinations([(1, 2), "invalid", (3, 4)])

def test_invalid_coordinate_length():
    with pytest.raises(TypeError, match="Each coordinate must be a tuple of two numeric values"):
        get_unique_coordinate_combinations([(1, 2, 3), (4, 5)])