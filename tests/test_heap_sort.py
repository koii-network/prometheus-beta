import pytest
from src.heap_sort import heap_sort

def test_heap_sort_normal_list():
    """Test heap sort with a normal unsorted list"""
    arr = [12, 11, 13, 5, 6, 7]
    expected = sorted(arr)
    assert heap_sort(arr) == expected

def test_heap_sort_already_sorted():
    """Test heap sort with an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert heap_sort(arr) == arr

def test_heap_sort_reverse_sorted():
    """Test heap sort with a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    expected = sorted(arr)
    assert heap_sort(arr) == expected

def test_heap_sort_empty_list():
    """Test heap sort with an empty list"""
    arr = []
    assert heap_sort(arr) == []

def test_heap_sort_single_element():
    """Test heap sort with a single-element list"""
    arr = [42]
    assert heap_sort(arr) == [42]

def test_heap_sort_negative_numbers():
    """Test heap sort with negative numbers"""
    arr = [-1, -5, 10, -3, 0]
    expected = sorted(arr)
    assert heap_sort(arr) == expected

def test_heap_sort_duplicate_numbers():
    """Test heap sort with duplicate numbers"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = sorted(arr)
    assert heap_sort(arr) == expected