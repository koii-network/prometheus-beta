import pytest
from src.unique_coordinate_combinations import get_unique_coordinate_combinations

def test_basic_coordinate_combinations():
    coords = [(1, 2), (3, 4), (2, 1)]
    result = get_unique_coordinate_combinations(coords)
    assert result == [1, 2, 3, 4]

def test_duplicate_coordinates():
    coords = [(1, 1), (1, 2), (2, 1), (2, 2)]
    result = get_unique_coordinate_combinations(coords)
    assert result == [1, 2]

def test_floating_point_coordinates():
    coords = [(1.5, 2.7), (3.2, 1.1), (2.7, 1.5)]
    result = get_unique_coordinate_combinations(coords)
    assert result == [1.1, 1.5, 2.7, 3.2]

def test_negative_coordinates():
    coords = [(-1, 2), (3, -4), (0, 0)]
    result = get_unique_coordinate_combinations(coords)
    assert result == [-4, -1, 0, 2, 3]

def test_empty_list():
    coords = []
    result = get_unique_coordinate_combinations(coords)
    assert result == []

def test_invalid_input_not_list():
    with pytest.raises(TypeError):
        get_unique_coordinate_combinations("not a list")

def test_invalid_coordinate_pair():
    with pytest.raises(ValueError):
        get_unique_coordinate_combinations([(1, 2), (3), (4, 5)])

def test_invalid_coordinate_type():
    with pytest.raises(ValueError):
        get_unique_coordinate_combinations([(1, 'a'), (2, 3)])