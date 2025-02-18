import pytest
from src.smooth_sort import smooth_sort

def test_smooth_sort_empty_list():
    """Test sorting an empty list"""
    assert smooth_sort([]) == []

def test_smooth_sort_single_element():
    """Test sorting a list with a single element"""
    assert smooth_sort([5]) == [5]

def test_smooth_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    assert smooth_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_smooth_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    assert smooth_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_smooth_sort_unsorted_list():
    """Test sorting a random unsorted list"""
    assert smooth_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

def test_smooth_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    assert smooth_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

def test_smooth_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert smooth_sort([-4, 2, -9, 0, 3, -1]) == [-9, -4, -1, 0, 2, 3]

def test_smooth_sort_large_list():
    """Test sorting a larger list"""
    large_list = [99, 45, 3, 87, 12, 56, 41, 23, 0, -5, 78, 31]
    assert smooth_sort(large_list) == sorted(large_list)