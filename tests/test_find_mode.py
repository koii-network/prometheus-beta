import pytest
from src.find_mode import find_mode

def test_single_mode():
    """Test finding a single mode"""
    assert find_mode([1, 2, 2, 3, 4]) == 2

def test_multiple_modes():
    """Test finding multiple modes"""
    assert set(find_mode([1, 2, 2, 3, 3, 4])) == {2, 3}

def test_empty_list():
    """Test behavior with an empty list"""
    assert find_mode([]) == []

def test_all_unique():
    """Test list with all unique elements"""
    assert find_mode([1, 2, 3, 4, 5]) in [1, 2, 3, 4, 5]

def test_float_numbers():
    """Test with float numbers"""
    assert find_mode([1.5, 2.5, 2.5, 3.5]) == 2.5

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        find_mode("not a list")

def test_single_element_list():
    """Test list with a single element"""
    assert find_mode([42]) == 42