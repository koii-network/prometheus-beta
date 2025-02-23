import pytest
from src.tim_sort import tim_sort

def test_empty_list():
    """Test sorting an empty list"""
    assert tim_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert tim_sort([5]) == [5]

def test_already_sorted_list():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert tim_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert tim_sort(input_list) == [1, 2, 3, 4, 5]

def test_random_list():
    """Test sorting a random list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert tim_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert tim_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_large_list():
    """Test sorting a larger list of integers"""
    input_list = list(range(100, 0, -1))
    assert tim_sort(input_list) == list(range(1, 101))

def test_list_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 0, 7, -1]
    assert tim_sort(input_list) == [-5, -2, -1, 0, 3, 7]

def test_original_list_unchanged():
    """Verify that the original list remains unchanged"""
    input_list = [5, 2, 9, 1, 7]
    original_copy = input_list.copy()
    tim_sort(input_list)
    assert input_list == original_copy

def test_list_with_floats():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    assert tim_sort(input_list) == [0.58, 1.41, 2.71, 3.14]