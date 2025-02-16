import pytest
from src.cartesian_tree_sort import cartesian_tree_sort

def test_cartesian_tree_sort_empty_list():
    """Test sorting an empty list"""
    assert cartesian_tree_sort([]) == []

def test_cartesian_tree_sort_single_element():
    """Test sorting a list with a single element"""
    assert cartesian_tree_sort([5]) == [5]

def test_cartesian_tree_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert cartesian_tree_sort(input_list) == [1, 2, 3, 4, 5]

def test_cartesian_tree_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert cartesian_tree_sort(input_list) == [1, 2, 3, 4, 5]

def test_cartesian_tree_sort_random_list():
    """Test sorting a random list of integers"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert cartesian_tree_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_cartesian_tree_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 3, 1, 1, 2, 2]
    assert cartesian_tree_sort(input_list) == [1, 1, 2, 2, 3, 3, 3]

def test_cartesian_tree_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 2, -3, 0, 1, -1]
    assert cartesian_tree_sort(input_list) == [-5, -3, -1, 0, 1, 2]