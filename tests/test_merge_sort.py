import pytest
from src.merge_sort import merge_sort

def test_merge_sort_empty_list():
    """Test sorting an empty list"""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test sorting a list with a single element"""
    assert merge_sort([5]) == [5]

def test_merge_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert merge_sort(input_list) == input_list

def test_merge_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert merge_sort(input_list) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted_list():
    """Test sorting an unsorted list"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert merge_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_merge_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert merge_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_merge_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 0, 1, -9]
    assert merge_sort(input_list) == [-9, -5, -2, 0, 1, 3]

def test_merge_sort_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        merge_sort("not a list")
    with pytest.raises(TypeError):
        merge_sort(12345)
    with pytest.raises(TypeError):
        merge_sort(None)