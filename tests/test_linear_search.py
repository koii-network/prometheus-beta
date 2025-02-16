import pytest
from src.linear_search import linear_search

def test_linear_search_found():
    """Test finding an existing element in the list"""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 3) == 2

def test_linear_search_not_found():
    """Test searching for an element not in the list"""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 6) == -1

def test_linear_search_first_element():
    """Test finding the first element in the list"""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 1) == 0

def test_linear_search_last_element():
    """Test finding the last element in the list"""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 5) == 4

def test_linear_search_empty_list():
    """Test searching in an empty list"""
    arr = []
    assert linear_search(arr, 1) == -1

def test_linear_search_multiple_occurrences():
    """Test that the first occurrence is returned"""
    arr = [1, 2, 3, 2, 1]
    assert linear_search(arr, 2) == 1

def test_linear_search_different_types():
    """Test searching with different data types"""
    arr = [1, "hello", 3.14, True]
    assert linear_search(arr, "hello") == 1
    assert linear_search(arr, 3.14) == 2