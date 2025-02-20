import pytest
from src.unique_sorted_list import get_unique_sorted_list

def test_unique_sorted_list_basic():
    """Test basic functionality of getting unique sorted list"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 2, 3, 4, 5, 6, 9]
    assert get_unique_sorted_list(input_list) == expected

def test_unique_sorted_list_already_sorted():
    """Test list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert get_unique_sorted_list(input_list) == [1, 2, 3, 4, 5]

def test_unique_sorted_list_empty():
    """Test empty list"""
    assert get_unique_sorted_list([]) == []

def test_unique_sorted_list_negative_numbers():
    """Test list with negative numbers"""
    input_list = [-3, -1, -4, 0, 1, 3]
    assert get_unique_sorted_list(input_list) == [-4, -3, -1, 0, 1, 3]

def test_unique_sorted_list_single_element():
    """Test list with a single element"""
    assert get_unique_sorted_list([42]) == [42]

def test_unique_sorted_list_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_sorted_list("not a list")

def test_unique_sorted_list_invalid_element_type():
    """Test raising TypeError for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        get_unique_sorted_list([1, 2, "3", 4])