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

def test_cartesian_tree_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert cartesian_tree_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_cartesian_tree_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 3, -2, 0, 7, -1]
    assert cartesian_tree_sort(arr) == [-5, -2, -1, 0, 3, 7]

def test_build_cartesian_tree():
    """Test the Cartesian tree building process"""
    arr = [3, 1, 4, 1, 5]
    root = build_cartesian_tree(arr)
    
    # Verify root and basic tree structure
    assert root is not None
    assert root.value == 3  # First element is root in this case

def test_build_cartesian_tree_empty():
    """Test building a Cartesian tree with an empty list"""
    assert build_cartesian_tree([]) is None