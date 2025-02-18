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
    assert strand_sort(input_list) == [1, 2, 3, 4, 5]

def test_strand_sort_reversed_list():
    """Test sorting a reversed list"""
    input_list = [5, 4, 3, 2, 1]
    assert strand_sort(input_list) == [1, 2, 3, 4, 5]

def test_strand_sort_random_list():
    """Test sorting a random list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert strand_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_strand_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert strand_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_strand_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 0, 1, -8]
    assert strand_sort(input_list) == [-8, -5, -2, 0, 1, 3]

def test_strand_sort_original_list_unchanged():
    """Ensure the original list is not modified"""
    input_list = [5, 2, 9, 1, 7]
    original_copy = input_list.copy()
    strand_sort(input_list)
    assert input_list == original_copy