import pytest
from src.local_max_finder import find_local_max_values

def test_basic_local_max():
    """Test finding local maximums in a typical array"""
    assert find_local_max_values([1, 3, 2, 4, 1, 5, 3]) == [3, 4, 5]

def test_ascending_array():
    """Test finding local max in a strictly ascending array"""
    assert find_local_max_values([1, 2, 3, 4, 5]) == [5]

def test_descending_array():
    """Test finding local max in a strictly descending array"""
    assert find_local_max_values([5, 4, 3, 2, 1]) == [5]

def test_empty_array():
    """Test behavior with an empty array"""
    assert find_local_max_values([]) == []

def test_single_element_array():
    """Test behavior with a single-element array"""
    assert find_local_max_values([1]) == []

def test_two_element_array():
    """Test finding local max in a two-element array"""
    assert find_local_max_values([2, 1]) == [2]
    assert find_local_max_values([1, 2]) == [2]

def test_all_same_elements():
    """Test array with all elements being the same"""
    assert find_local_max_values([3, 3, 3, 3]) == []

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        find_local_max_values("not a list")

def test_invalid_element_type():
    """Test raising ValueError for non-integer elements"""
    with pytest.raises(ValueError):
        find_local_max_values([1, 2, 'a', 4])