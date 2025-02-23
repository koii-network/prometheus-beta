import pytest
from src.binary_search import binary_search

def test_basic_search():
    """Test basic binary search functionality"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 13) == 6

def test_element_not_found():
    """Test searching for non-existent elements"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 14) == -1
    assert binary_search(arr, 6) == -1

def test_empty_list():
    """Test binary search on an empty list"""
    assert binary_search([], 5) == -1

def test_single_element_list():
    """Test binary search on a single-element list"""
    arr = [5]
    assert binary_search(arr, 5) == 0
    assert binary_search(arr, 6) == -1

def test_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    
    with pytest.raises(ValueError):
        binary_search([5, 3, 1], 3)

def test_repeated_elements():
    """Test binary search with repeated elements"""
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    # Note: This implementation returns the first occurrence of the target
    assert binary_search(arr, 3) in [3, 4, 5]
    assert binary_search(arr, 2) in [1, 2]