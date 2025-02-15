import pytest
from src.exponential_search import exponential_search

def test_exponential_search_basic():
    """Test basic functionality of exponential search"""
    arr = [1, 3, 4, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 7) == 4
    assert exponential_search(arr, 1) == 0
    assert exponential_search(arr, 15) == 8

def test_exponential_search_not_found():
    """Test when element is not in the array"""
    arr = [1, 3, 4, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 6) == -1
    assert exponential_search(arr, 0) == -1
    assert exponential_search(arr, 16) == -1

def test_exponential_search_empty_list():
    """Test searching in an empty list"""
    arr = []
    assert exponential_search(arr, 5) == -1

def test_exponential_search_single_element():
    """Test searching in a single-element list"""
    arr = [5]
    assert exponential_search(arr, 5) == 0
    assert exponential_search(arr, 6) == -1

def test_exponential_search_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        exponential_search(None, 5)
    with pytest.raises(TypeError):
        exponential_search("not a list", 5)
    with pytest.raises(TypeError):
        exponential_search(123, 5)