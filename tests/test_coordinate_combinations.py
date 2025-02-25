import pytest
from src.coordinate_combinations import get_unique_coordinate_combinations

def test_basic_coordinate_combinations():
    """Test basic functionality with a simple list of coordinates"""
    coords = [(1, 2), (3, 4), (1, 4), (3, 2)]
    result = get_unique_coordinate_combinations(coords)
    assert result == [(1, 2), (1, 4), (3, 2), (3, 4)]

def test_duplicate_coordinates():
    """Test handling of duplicate coordinates"""
    coords = [(1, 2), (1, 2), (3, 4), (3, 4)]
    result = get_unique_coordinate_combinations(coords)
    assert result == [(1, 2), (1, 4), (3, 2), (3, 4)]

def test_single_coordinate():
    """Test scenario with a single coordinate"""
    coords = [(5, 5)]
    result = get_unique_coordinate_combinations(coords)
    assert result == [(5, 5)]

def test_empty_list():
    """Test behavior with an empty list"""
    coords = []
    result = get_unique_coordinate_combinations(coords)
    assert result == []

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        get_unique_coordinate_combinations("not a list")
    
    with pytest.raises(TypeError):
        get_unique_coordinate_combinations(None)

def test_invalid_coordinate_pairs():
    """Test handling of invalid coordinate pairs"""
    with pytest.raises(ValueError):
        get_unique_coordinate_combinations([(1,), (2, 3), (4)])
    
    with pytest.raises(ValueError):
        get_unique_coordinate_combinations([(1, 2), 'invalid', (3, 4)])

def test_unsorted_input():
    """Test that coordinates are correctly sorted"""
    coords = [(3, 1), (1, 4), (2, 2)]
    result = get_unique_coordinate_combinations(coords)
    assert result == [(1, 1), (1, 2), (1, 4), (2, 1), (2, 2), (2, 4), (3, 1), (3, 2), (3, 4)]