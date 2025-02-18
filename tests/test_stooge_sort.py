import pytest
from src.stooge_sort import stooge_sort

def test_stooge_sort_empty_list():
    """Test sorting an empty list"""
    assert stooge_sort([]) == []

def test_stooge_sort_single_element():
    """Test sorting a list with a single element"""
    assert stooge_sort([42]) == [42]

def test_stooge_sort_already_sorted():
    """Test sorting a list that's already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert stooge_sort(arr) == [1, 2, 3, 4, 5]

def test_stooge_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert stooge_sort(arr) == [1, 2, 3, 4, 5]

def test_stooge_sort_unsorted_list():
    """Test sorting a random unsorted list"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert stooge_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_stooge_sort_with_duplicates():
    """Test sorting a list with duplicate values"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert stooge_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_stooge_sort_preserves_original():
    """Test that the original list is not modified"""
    arr = [5, 2, 9, 1, 7]
    original = arr.copy()
    stooge_sort(arr)
    assert arr == original

def test_stooge_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 2, -10, 0, 7, -3]
    assert stooge_sort(arr) == [-10, -5, -3, 0, 2, 7]