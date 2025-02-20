import pytest
from src.bubble_sort import optimized_bubble_sort

def test_optimized_bubble_sort_normal_case():
    """Test sorting a normal unsorted list"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    result = optimized_bubble_sort(input_list.copy())
    assert result == expected, "Should sort the list correctly"

def test_optimized_bubble_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    expected = input_list.copy()
    result = optimized_bubble_sort(input_list.copy())
    assert result == expected, "Should return the same list if already sorted"

def test_optimized_bubble_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    result = optimized_bubble_sort(input_list.copy())
    assert result == expected, "Should correctly sort a reverse-sorted list"

def test_optimized_bubble_sort_empty_list():
    """Test sorting an empty list"""
    input_list = []
    expected = []
    result = optimized_bubble_sort(input_list)
    assert result == expected, "Should handle empty list"

def test_optimized_bubble_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    expected = [42]
    result = optimized_bubble_sort(input_list)
    assert result == expected, "Should handle single-element list"

def test_optimized_bubble_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    result = optimized_bubble_sort(input_list.copy())
    assert result == expected, "Should handle lists with duplicate elements"