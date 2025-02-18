import pytest
from src.tim_sort import tim_sort

def test_tim_sort_empty_list():
    """Test sorting an empty list"""
    assert tim_sort([]) == []

def test_tim_sort_single_element():
    """Test sorting a list with a single element"""
    assert tim_sort([5]) == [5]

def test_tim_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert tim_sort(input_list) == [1, 2, 3, 4, 5]

def test_tim_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert tim_sort(input_list) == [1, 2, 3, 4, 5]

def test_tim_sort_random_list():
    """Test sorting a list with random elements"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert tim_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_tim_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert tim_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_tim_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-4, 2, -9, 0, 5, -1]
    assert tim_sort(input_list) == [-9, -4, -1, 0, 2, 5]

def test_tim_sort_preserves_original_list():
    """Test that the original list is not modified"""
    input_list = [5, 3, 2, 1, 4]
    original_copy = input_list.copy()
    tim_sort(input_list)
    assert input_list == original_copy