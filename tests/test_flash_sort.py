import pytest
from src.flash_sort import flash_sort

def test_flash_sort_empty_list():
    """Test sorting an empty list"""
    assert flash_sort([]) == []

def test_flash_sort_single_element():
    """Test sorting a single element list"""
    assert flash_sort([5]) == [5]

def test_flash_sort_multiple_elements():
    """Test sorting a list with multiple elements"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert flash_sort(input_list) == sorted(input_list)

def test_flash_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [5, 5, 5, 3, 3, 1, 1]
    assert flash_sort(input_list) == sorted(input_list)

def test_flash_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-4, 2, -7, 1, 0, -3, 5]
    assert flash_sort(input_list) == sorted(input_list)

def test_flash_sort_large_range():
    """Test sorting a list with a large range of values"""
    input_list = [1000, 1, 100000, 10, 50, 500, 5000]
    assert flash_sort(input_list) == sorted(input_list)

def test_flash_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5, 6, 7]
    assert flash_sort(input_list) == input_list

def test_flash_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [7, 6, 5, 4, 3, 2, 1]
    assert flash_sort(input_list) == sorted(input_list)