import pytest
from src.binary_search import binary_search

def test_binary_search_found():
    """Test finding an existing element in the middle of the array"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3

def test_binary_search_first_element():
    """Test finding the first element in the array"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 1) == 0

def test_binary_search_last_element():
    """Test finding the last element in the array"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 13) == 6

def test_binary_search_not_found():
    """Test searching for an element not in the array"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 4) == -1

def test_binary_search_empty_list():
    """Test searching in an empty list"""
    arr = []
    assert binary_search(arr, 5) == -1

def test_binary_search_single_element_found():
    """Test searching in a single-element list where the element is found"""
    arr = [5]
    assert binary_search(arr, 5) == 0

def test_binary_search_single_element_not_found():
    """Test searching in a single-element list where the element is not found"""
    arr = [5]
    assert binary_search(arr, 6) == -1

def test_binary_search_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        binary_search("not a list", 5)

def test_binary_search_unsorted_list():
    """Test that a ValueError is raised for an unsorted list"""
    with pytest.raises(ValueError, match="Input list must be sorted in ascending order"):
        binary_search([5, 3, 1], 3)