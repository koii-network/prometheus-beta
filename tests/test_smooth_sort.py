import pytest
from src.smooth_sort import smooth_sort

def test_smooth_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert smooth_sort(arr) == []

def test_smooth_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert smooth_sort(arr) == [42]

def test_smooth_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert smooth_sort(arr) == [1, 2, 3, 4, 5]

def test_smooth_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert smooth_sort(arr) == [1, 2, 3, 4, 5]

def test_smooth_sort_random_list():
    """Test sorting a random list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert smooth_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_smooth_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert smooth_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_smooth_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 3, -2, 7, 0, -1, 8]
    assert smooth_sort(arr) == [-5, -2, -1, 0, 3, 7, 8]