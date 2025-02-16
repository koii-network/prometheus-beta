import pytest
from src.binary_search import binary_search

def test_binary_search_normal_case():
    """Test binary search on a typical sorted list."""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 13) == 6

def test_binary_search_first_element():
    """Test finding the first element."""
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 1) == 0

def test_binary_search_last_element():
    """Test finding the last element."""
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 9) == 4

def test_binary_search_not_found():
    """Test when element is not in the list."""
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 4) == -1
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 10) == -1

def test_binary_search_empty_list():
    """Test binary search on an empty list."""
    arr = []
    assert binary_search(arr, 5) == -1

def test_binary_search_single_element_found():
    """Test binary search on a single-element list where target is found."""
    arr = [5]
    assert binary_search(arr, 5) == 0

def test_binary_search_single_element_not_found():
    """Test binary search on a single-element list where target is not found."""
    arr = [5]
    assert binary_search(arr, 6) == -1

def test_binary_search_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        binary_search("not a list", 5)

def test_binary_search_unsorted_list():
    """Test raising ValueError for unsorted list."""
    with pytest.raises(ValueError, match="Input list must be sorted in ascending order"):
        binary_search([5, 3, 1, 4], 3)