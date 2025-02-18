import pytest
from src.cartesian_tree_sort import cartesian_tree_sort, build_cartesian_tree, Node

def test_cartesian_tree_sort_empty_list():
    """Test sorting an empty list"""
    assert cartesian_tree_sort([]) == []

def test_cartesian_tree_sort_single_element():
    """Test sorting a list with a single element"""
    assert cartesian_tree_sort([5]) == [5]

def test_cartesian_tree_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert cartesian_tree_sort(arr) == arr

def test_cartesian_tree_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert cartesian_tree_sort(arr) == [1, 2, 3, 4, 5]

def test_cartesian_tree_sort_random_list():
    """Test sorting a random list of integers"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 3, 3, 1, 1, 4, 4]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 0, 3, -2, 8, -1]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_build_cartesian_tree_root():
    """Test building a Cartesian tree and checking its root"""
    arr = [3, 1, 4, 1, 5]
    root = build_cartesian_tree(arr)
    assert root.value == 5  # Maximum element is the root