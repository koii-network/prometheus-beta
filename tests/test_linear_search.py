import pytest
from src.linear_search import linear_search

def test_linear_search_basic():
    """Test basic functionality of linear search"""
    arr = [4, 2, 7, 1, 5, 3]
    assert linear_search(arr, 7) == 2  # 7 is at index 2
    assert linear_search(arr, 1) == 3  # 1 is at index 3

def test_linear_search_first_element():
    """Test when target is the first element"""
    arr = [5, 2, 3, 4, 1]
    assert linear_search(arr, 5) == 0

def test_linear_search_last_element():
    """Test when target is the last element"""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 5) == 4

def test_linear_search_not_found():
    """Test when target is not in the array"""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 6) == -1

def test_linear_search_empty_array():
    """Test searching in an empty array"""
    arr = []
    assert linear_search(arr, 1) == -1

def test_linear_search_multiple_occurrences():
    """Test when target appears multiple times"""
    arr = [1, 2, 3, 2, 4, 2]
    assert linear_search(arr, 2) == 1  # Returns the first occurrence