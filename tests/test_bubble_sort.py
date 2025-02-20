import pytest
from src.bubble_sort import optimized_bubble_sort

def test_optimized_bubble_sort_normal_list():
    """Test sorting a normal unsorted list"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_optimized_bubble_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    expected = input_list.copy()
    assert optimized_bubble_sort(input_list) == expected

def test_optimized_bubble_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_optimized_bubble_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_optimized_bubble_sort_empty_list():
    """Test sorting an empty list"""
    input_list = []
    expected = []
    assert optimized_bubble_sort(input_list) == expected

def test_optimized_bubble_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    expected = [42]
    assert optimized_bubble_sort(input_list) == expected

def test_optimized_bubble_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, -2, -8, -1, -9]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected