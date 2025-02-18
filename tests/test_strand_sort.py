import pytest
from src.strand_sort import strand_sort

def test_strand_sort_empty_list():
    """Test sorting an empty list"""
    assert strand_sort([]) == []

def test_strand_sort_single_element():
    """Test sorting a list with a single element"""
    assert strand_sort([5]) == [5]

def test_strand_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert strand_sort(input_list) == input_list

def test_strand_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert strand_sort(input_list) == [1, 2, 3, 4, 5]

def test_strand_sort_random_order():
    """Test sorting a list in random order"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert strand_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_strand_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 2, 1, 4, 3]
    assert strand_sort(input_list) == [1, 2, 3, 3, 3, 4]

def test_strand_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 0, 7, -1]
    assert strand_sort(input_list) == [-5, -2, -1, 0, 3, 7]

def test_strand_sort_large_list():
    """Test sorting a large list to check performance"""
    input_list = list(range(100, 0, -1))  # Reverse sorted list
    assert strand_sort(input_list) == list(range(1, 101))