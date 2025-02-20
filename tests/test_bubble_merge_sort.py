import pytest
from src.bubble_merge_sort import bubble_merge_sort

def test_bubble_merge_sort_normal_case():
    """Test sorting a standard list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_merge_sort(arr) == sorted(arr)

def test_bubble_merge_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert bubble_merge_sort(arr) == []

def test_bubble_merge_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert bubble_merge_sort(arr) == [42]

def test_bubble_merge_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert bubble_merge_sort(arr) == [1, 2, 3, 4, 5]

def test_bubble_merge_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert bubble_merge_sort(arr) == [1, 2, 3, 4, 5]

def test_bubble_merge_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bubble_merge_sort(arr) == sorted(arr)

def test_bubble_merge_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-3, 4, -1, 7, -5, 2, 0]
    assert bubble_merge_sort(arr) == sorted(arr)