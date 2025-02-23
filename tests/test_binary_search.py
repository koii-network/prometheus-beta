import pytest
from src.binary_search import binary_search

def test_binary_search_found():
    """Test finding an existing element in the middle of the array"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3

def test_binary_search_first_element():
    """Test finding the first element"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 1) == 0

def test_binary_search_last_element():
    """Test finding the last element"""
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
    """Test searching in a single-element list where element is found"""
    arr = [5]
    assert binary_search(arr, 5) == 0

def test_binary_search_single_element_not_found():
    """Test searching in a single-element list where element is not found"""
    arr = [5]
    assert binary_search(arr, 6) == -1

def test_binary_search_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        binary_search("not a list", 5)

def test_binary_search_unsorted_list():
    """Test raising ValueError for unsorted list"""
    with pytest.raises(ValueError, match="Input list must be sorted in ascending order"):
        binary_search([5, 3, 1, 7, 9], 5)

def test_binary_search_duplicate_elements():
    """Test behavior with duplicate elements"""
    arr = [1, 2, 2, 3, 4, 4, 5]
    result = binary_search(arr, 2)
    assert result in [1, 2]  # Either index of the first or second 2 is acceptable