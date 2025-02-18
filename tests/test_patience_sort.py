import pytest
from src.patience_sort import patience_sort

def test_patience_sort_empty_list():
    """Test sorting an empty list"""
    assert patience_sort([]) == []

def test_patience_sort_single_element():
    """Test sorting a list with a single element"""
    assert patience_sort([5]) == [5]

def test_patience_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert patience_sort(input_list) == input_list

def test_patience_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert patience_sort(input_list) == [1, 2, 3, 4, 5]

def test_patience_sort_random_integers():
    """Test sorting a list of random integers"""
    input_list = [34, 15, 88, 2, 23, 57, 42, 11]
    assert patience_sort(input_list) == sorted(input_list)

def test_patience_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert patience_sort(input_list) == sorted(input_list)

def test_patience_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 0, -1, 7, 4]
    assert patience_sort(input_list) == sorted(input_list)

def test_patience_sort_floating_point():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert patience_sort(input_list) == sorted(input_list)

def test_patience_sort_preserves_original_list():
    """Test that the original list is not modified"""
    input_list = [5, 2, 8, 1, 9]
    _ = patience_sort(input_list)
    assert input_list == [5, 2, 8, 1, 9]