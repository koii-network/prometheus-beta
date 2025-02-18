import pytest
from src.linear_search import linear_search

def test_linear_search_found():
    """Test finding an existing element in the list"""
    arr = [4, 2, 7, 1, 5, 3]
    assert linear_search(arr, 7) == 2  # 7 is at index 2
    assert linear_search(arr, 1) == 3  # 1 is at index 3

def test_linear_search_not_found():
    """Test searching for an element not in the list"""
    arr = [4, 2, 7, 1, 5, 3]
    assert linear_search(arr, 10) == -1  # 10 is not in the list

def test_linear_search_empty_list():
    """Test searching in an empty list"""
    arr = []
    assert linear_search(arr, 5) == -1

def test_linear_search_first_element():
    """Test finding the first element"""
    arr = [4, 2, 7, 1, 5, 3]
    assert linear_search(arr, 4) == 0

def test_linear_search_last_element():
    """Test finding the last element"""
    arr = [4, 2, 7, 1, 5, 3]
    assert linear_search(arr, 3) == 5

def test_linear_search_multiple_occurrences():
    """Test when there are multiple occurrences of the target"""
    arr = [4, 2, 7, 2, 1, 5, 3]
    assert linear_search(arr, 2) == 1  # Returns the first occurrence