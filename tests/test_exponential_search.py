import pytest
from src.exponential_search import exponential_search

def test_exponential_search_found():
    """Test finding an element in the middle of the list"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 7) == 3

def test_exponential_search_first_element():
    """Test finding the first element"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 1) == 0

def test_exponential_search_last_element():
    """Test finding the last element"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 15) == 7

def test_exponential_search_not_found():
    """Test when element is not in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 10) == -1

def test_exponential_search_empty_list():
    """Test raising ValueError for empty list"""
    with pytest.raises(ValueError):
        exponential_search([], 5)

def test_exponential_search_invalid_input():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        exponential_search("not a list", 5)