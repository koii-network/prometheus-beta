import pytest
from src.tim_sort import tim_sort

def test_tim_sort_basic():
    """Test basic sorting of a list of integers"""
    input_list = [5, 2, 9, 1, 7, 6, 3]
    expected = sorted(input_list)
    assert tim_sort(input_list) == expected

def test_tim_sort_empty_list():
    """Test sorting an empty list"""
    assert tim_sort([]) == []

def test_tim_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert tim_sort(input_list) == input_list

def test_tim_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert tim_sort(input_list) == expected

def test_tim_sort_with_duplicates():
    """Test sorting a list with duplicate values"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert tim_sort(input_list) == expected

def test_tim_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 2, -10, 0, 7, -3, 8]
    expected = sorted(input_list)
    assert tim_sort(input_list) == expected

def test_tim_sort_preserves_original_list():
    """Test that the original list is not modified"""
    input_list = [5, 2, 9, 1, 7]
    original_copy = input_list.copy()
    tim_sort(input_list)
    assert input_list == original_copy