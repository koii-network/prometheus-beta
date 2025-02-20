import pytest
from src.bubble_sort import optimized_bubble_sort

def test_optimized_bubble_sort_normal_case():
    """Test sorting a standard list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert optimized_bubble_sort(arr) == sorted(arr)

def test_optimized_bubble_sort_already_sorted():
    """Test an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert optimized_bubble_sort(arr) == arr

def test_optimized_bubble_sort_reverse_sorted():
    """Test a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert optimized_bubble_sort(arr) == sorted(arr)

def test_optimized_bubble_sort_empty_list():
    """Test an empty list"""
    arr = []
    assert optimized_bubble_sort(arr) == []

def test_optimized_bubble_sort_single_element():
    """Test a list with a single element"""
    arr = [42]
    assert optimized_bubble_sort(arr) == [42]

def test_optimized_bubble_sort_duplicate_elements():
    """Test a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert optimized_bubble_sort(arr) == sorted(arr)

def test_optimized_bubble_sort_not_modify_original():
    """Ensure the original list is not modified"""
    arr = [5, 2, 9, 1, 7]
    original = arr.copy()
    optimized_bubble_sort(arr)
    assert arr == original