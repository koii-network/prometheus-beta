import pytest
from src.flash_sort import flash_sort

def test_flash_sort_empty_list():
    """Test sorting an empty list"""
    assert flash_sort([]) == []

def test_flash_sort_single_element():
    """Test sorting a list with a single element"""
    assert flash_sort([5]) == [5]

def test_flash_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert flash_sort(input_list) == input_list

def test_flash_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert flash_sort(input_list) == [1, 2, 3, 4, 5]

def test_flash_sort_random_list():
    """Test sorting a random list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert flash_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_flash_sort_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert flash_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_flash_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-4, 2, -1, 0, 5, -3]
    assert flash_sort(input_list) == [-4, -3, -1, 0, 2, 5]

def test_flash_sort_large_range():
    """Test sorting a list with a large range of values"""
    input_list = [1000, 10, 100000, 1, 10000, 100]
    assert flash_sort(input_list) == [1, 10, 100, 1000, 10000, 100000]

def test_flash_sort_all_same_elements():
    """Test sorting a list with all elements being the same"""
    input_list = [7, 7, 7, 7, 7]
    assert flash_sort(input_list) == [7, 7, 7, 7, 7]