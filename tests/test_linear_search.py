import pytest
from src.linear_search import linear_search

def test_linear_search_existing_element():
    """Test finding an existing element in the list"""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 3) == 2
    assert linear_search(arr, 1) == 0
    assert linear_search(arr, 5) == 4

def test_linear_search_non_existing_element():
    """Test searching for a non-existing element"""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 6) == -1
    assert linear_search(arr, 0) == -1

def test_linear_search_empty_list():
    """Test searching in an empty list"""
    arr = []
    assert linear_search(arr, 1) == -1

def test_linear_search_multiple_occurrences():
    """Test when the target appears multiple times"""
    arr = [1, 2, 3, 2, 4, 2]
    assert linear_search(arr, 2) == 1  # Returns the first occurrence

def test_linear_search_different_types():
    """Test searching with different types of elements"""
    arr = [1, 'a', True, 3.14, None]
    assert linear_search(arr, 'a') == 1
    assert linear_search(arr, True) == 2
    assert linear_search(arr, 3.14) == 3
    assert linear_search(arr, None) == 4