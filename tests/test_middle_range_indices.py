import pytest
from src.middle_range_indices import find_middle_range_indices

def test_odd_length_list_default_radius():
    """Test finding indices for a list with odd number of elements using default radius."""
    test_list = [1, 2, 3, 4, 5, 6, 7]
    result = find_middle_range_indices(test_list)
    assert result == [2, 3, 4]

def test_even_length_list_default_radius():
    """Test finding indices for a list with even number of elements using default radius."""
    test_list = [1, 2, 3, 4, 5, 6]
    result = find_middle_range_indices(test_list)
    assert result == [1, 2, 3]

def test_custom_radius():
    """Test finding indices with a custom radius."""
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = find_middle_range_indices(test_list, range_radius=2)
    assert result == [2, 3, 4, 5, 6]

def test_zero_radius():
    """Test finding indices with zero radius."""
    test_list = [1, 2, 3, 4, 5]
    result = find_middle_range_indices(test_list, range_radius=0)
    assert result == [2]

def test_radius_larger_than_list():
    """Test when radius is larger than list length."""
    test_list = [1, 2, 3]
    result = find_middle_range_indices(test_list, range_radius=5)
    assert result == [0, 1, 2]

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_middle_range_indices([])

def test_invalid_input_type():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_middle_range_indices("not a list")

def test_invalid_radius_type():
    """Test that invalid radius type raises a TypeError."""
    with pytest.raises(TypeError, match="Range radius must be a non-negative integer"):
        find_middle_range_indices([1, 2, 3], range_radius=-1)
    
    with pytest.raises(TypeError, match="Range radius must be a non-negative integer"):
        find_middle_range_indices([1, 2, 3], range_radius="invalid")