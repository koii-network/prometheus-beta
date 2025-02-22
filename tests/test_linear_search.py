import pytest
from src.linear_search import linear_search

def test_linear_search_found():
    """Test finding an existing element in the list"""
    arr = [4, 2, 7, 1, 5, 3]
    assert linear_search(arr, 7) == 2

def test_linear_search_not_found():
    """Test searching for an element not in the list"""
    arr = [4, 2, 7, 1, 5, 3]
    assert linear_search(arr, 8) == -1

def test_linear_search_first_element():
    """Test finding the first element in the list"""
    arr = [4, 2, 7, 1, 5, 3]
    assert linear_search(arr, 4) == 0

def test_linear_search_last_element():
    """Test finding the last element in the list"""
    arr = [4, 2, 7, 1, 5, 3]
    assert linear_search(arr, 3) == 5

def test_linear_search_empty_list():
    """Test searching in an empty list"""
    arr = []
    assert linear_search(arr, 5) == -1

def test_linear_search_multiple_occurrences():
    """Test finding the first occurrence when multiple exist"""
    arr = [4, 2, 7, 2, 1, 5, 3]
    assert linear_search(arr, 2) == 1