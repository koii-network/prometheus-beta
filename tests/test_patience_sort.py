import pytest
from src.patience_sort import patience_sort

def test_patience_sort_empty_list():
    """Test sorting an empty list"""
    assert patience_sort([]) == []

def test_patience_sort_single_element():
    """Test sorting a list with a single element"""
    assert patience_sort([5]) == [5]

def test_patience_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert patience_sort(arr) == arr

def test_patience_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert patience_sort(arr) == [1, 2, 3, 4, 5]

def test_patience_sort_random_list():
    """Test sorting a random list of integers"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_floating_point():
    """Test sorting a list of floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert patience_sort(arr) == sorted(arr)

def test_patience_sort_strings():
    """Test sorting a list of strings"""
    arr = ['banana', 'apple', 'cherry', 'date']
    assert patience_sort(arr) == sorted(arr)