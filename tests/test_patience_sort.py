import pytest
from src.patience_sort import patience_sort

def test_patience_sort_basic():
    """Test basic sorting of integers"""
    arr = [5, 2, 8, 12, 1, 3]
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert patience_sort(arr) == []

def test_patience_sort_single_element():
    """Test sorting a single-element list"""
    arr = [42]
    assert patience_sort(arr) == [42]

def test_patience_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert patience_sort(arr) == arr

def test_patience_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_with_strings():
    """Test sorting a list of strings"""
    arr = ["banana", "apple", "cherry", "date"]
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 2, -8, 12, -1, 3]
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_large_list():
    """Test sorting a larger list"""
    arr = list(range(100, 0, -1))
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_preserves_original():
    """Test that the original list is not modified"""
    arr = [5, 2, 8, 12, 1, 3]
    original = arr.copy()
    patience_sort(arr)
    assert arr == original