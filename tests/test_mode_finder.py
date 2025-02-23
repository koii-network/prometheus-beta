import pytest
from src.mode_finder import find_mode

def test_single_mode():
    """Test finding a single mode"""
    assert find_mode([1, 2, 2, 3, 4]) == 2

def test_multiple_modes():
    """Test finding multiple modes"""
    assert sorted(find_mode([1, 1, 2, 2, 3])) == [1, 2]

def test_empty_list():
    """Test handling of empty list"""
    assert find_mode([]) == []

def test_all_unique():
    """Test list with all unique elements"""
    assert find_mode([1, 2, 3, 4, 5]) == 1

def test_single_element():
    """Test list with a single element"""
    assert find_mode([42]) == 42

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_mode(42)

def test_non_integer_elements():
    """Test raising ValueError for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        find_mode([1, 2, 'three', 4])

def test_large_list():
    """Test mode in a larger list"""
    large_list = [1] * 5 + [2] * 3 + [3] * 2
    assert find_mode(large_list) == 1