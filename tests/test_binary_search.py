import pytest
from src.binary_search import binary_search

def test_binary_search_existing_element():
    """Test finding an existing element in the middle of the list"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3

def test_binary_search_first_element():
    """Test finding the first element in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 1) == 0

def test_binary_search_last_element():
    """Test finding the last element in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 13) == 6

def test_binary_search_element_not_found():
    """Test when the element is not in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 6) == -1

def test_binary_search_empty_list():
    """Test binary search on an empty list"""
    arr = []
    assert binary_search(arr, 5) == -1

def test_binary_search_single_element_found():
    """Test binary search on a single-element list where element is found"""
    arr = [5]
    assert binary_search(arr, 5) == 0

def test_binary_search_single_element_not_found():
    """Test binary search on a single-element list where element is not found"""
    arr = [5]
    assert binary_search(arr, 6) == -1

def test_binary_search_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        binary_search("not a list", 5)

def test_binary_search_unsorted_list():
    """Test that ValueError is raised for unsorted list"""
    with pytest.raises(ValueError):
        binary_search([5, 3, 1, 4, 2], 3)