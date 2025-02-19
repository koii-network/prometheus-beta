import pytest
from src.library_sort import library_sort

def test_library_sort_empty_list():
    """Test sorting an empty list"""
    assert library_sort([]) == []

def test_library_sort_single_element():
    """Test sorting a list with a single element"""
    assert library_sort([5]) == [5]

def test_library_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert library_sort(input_list) == input_list

def test_library_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert library_sort(input_list) == [1, 2, 3, 4, 5]

def test_library_sort_random_list():
    """Test sorting a random list of integers"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_with_strings():
    """Test sorting a list of strings"""
    input_list = ["banana", "apple", "cherry", "date"]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_mixed_types():
    """Test sorting a list with mixed comparable types"""
    input_list = [3, "a", 1, "b", 2]
    assert library_sort(input_list) == sorted(input_list)

def test_library_sort_large_list():
    """Test sorting a larger list"""
    import random
    large_list = [random.randint(1, 1000) for _ in range(100)]
    assert library_sort(large_list) == sorted(large_list)