import pytest
from src.coordinate_combinations import get_unique_coordinate_combinations

def test_basic_coordinate_combinations():
    """Test basic functionality with simple coordinate pairs."""
    input_coords = [(1, 2), (3, 4), (1, 4), (3, 2)]
    expected = [[1, 2], [1, 4], [3, 2], [3, 4]]
    assert get_unique_coordinate_combinations(input_coords) == expected

def test_duplicate_coordinates():
    """Test handling of duplicate coordinates."""
    input_coords = [(1, 1), (1, 1), (2, 2), (2, 2)]
    expected = [[1, 1], [1, 2], [2, 1], [2, 2]]
    assert get_unique_coordinate_combinations(input_coords) == expected

def test_single_coordinate():
    """Test with a single coordinate pair."""
    input_coords = [(5, 5)]
    expected = [[5, 5]]
    assert get_unique_coordinate_combinations(input_coords) == expected

def test_empty_list():
    """Test with an empty list of coordinates."""
    assert get_unique_coordinate_combinations([]) == []

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list of coordinate pairs"):
        get_unique_coordinate_combinations("not a list")

def test_invalid_coordinate_type():
    """Test error handling for invalid coordinate pairs."""
    with pytest.raises(TypeError, match="Each coordinate must be a pair"):
        get_unique_coordinate_combinations([(1, 2), "invalid", (3, 4)])

def test_negative_coordinates():
    """Test handling of negative coordinates."""
    input_coords = [(-1, 2), (0, -3), (1, 0)]
    expected = [[-1, -3], [-1, 0], [-1, 2], [0, -3], [0, 0], [0, 2], [1, -3], [1, 0], [1, 2]]
    assert get_unique_coordinate_combinations(input_coords) == expected