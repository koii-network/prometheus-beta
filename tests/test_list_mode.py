import pytest
from src.list_mode import find_mode

def test_single_mode():
    """Test finding a single mode in a list"""
    assert find_mode([1, 2, 2, 3, 4]) == 2

def test_multiple_modes():
    """Test finding multiple modes in a list"""
    assert set(find_mode([1, 2, 2, 3, 3, 4])) == {2, 3}

def test_empty_list():
    """Test handling of an empty list"""
    assert find_mode([]) is None

def test_all_unique():
    """Test list with all unique elements"""
    assert find_mode([1, 2, 3, 4, 5]) == 1  # First element when all are unique

def test_floats():
    """Test mode with floating point numbers"""
    assert find_mode([1.5, 2.3, 1.5, 3.7]) == 1.5

def test_invalid_input():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        find_mode("not a list")

def test_single_element_list():
    """Test mode for a single element list"""
    assert find_mode([42]) == 42