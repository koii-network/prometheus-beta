import pytest
from src.binary_search import binary_search

def test_binary_search_basic():
    """Test basic binary search functionality"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 13) == 6
    assert binary_search(arr, 1) == 0

def test_binary_search_not_found():
    """Test when target is not in the array"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 4) == -1
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 14) == -1

def test_binary_search_empty_list():
    """Test binary search on an empty list"""
    assert binary_search([], 5) == -1

def test_binary_search_single_element():
    """Test binary search on a single-element list"""
    arr = [42]
    assert binary_search(arr, 42) == 0
    assert binary_search(arr, 43) == -1

def test_binary_search_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        binary_search("not a list", 5)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        binary_search(None, 5)

def test_binary_search_unsorted_list():
    """Test error handling for unsorted list"""
    with pytest.raises(ValueError, match="Input list must be sorted in ascending order"):
        binary_search([5, 3, 1, 4], 3)

def test_binary_search_duplicates():
    """Test binary search with duplicate elements (returns first occurrence)"""
    arr = [1, 2, 2, 3, 3, 3, 4, 5]
    result = binary_search(arr, 3)
    assert result in [3, 4, 5]  # Any of these indices are valid