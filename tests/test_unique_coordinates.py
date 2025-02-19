import pytest
from src.unique_coordinates import get_unique_coordinate_combinations

def test_basic_coordinate_combinations():
    coordinates = [(1, 2), (3, 4), (1, 4), (3, 2)]
    expected = [(1, 2), (1, 4), (3, 2), (3, 4)]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_duplicate_coordinates():
    coordinates = [(1, 1), (1, 1), (2, 2), (2, 2)]
    expected = [(1, 1), (1, 2), (2, 1), (2, 2)]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_single_coordinate():
    coordinates = [(5, 5)]
    expected = [(5, 5)]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_empty_list():
    coordinates = []
    expected = []
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_invalid_input_not_list():
    with pytest.raises(TypeError, match="Input must be a list of coordinate pairs"):
        get_unique_coordinate_combinations("not a list")

def test_invalid_coordinate_pairs():
    with pytest.raises(TypeError, match="Each coordinate must be a pair"):
        get_unique_coordinate_combinations([(1,), (2, 3, 4)])

def test_mixed_input_types():
    coordinates = [(1, 2), (3.5, 4), (2, "test")]
    with pytest.raises(TypeError, match="Each coordinate must be a pair"):
        get_unique_coordinate_combinations(coordinates)