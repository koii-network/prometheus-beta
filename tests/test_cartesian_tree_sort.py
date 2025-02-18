import pytest
from src.cartesian_tree_sort import cartesian_tree_sort, build_cartesian_tree, Node

def test_cartesian_tree_sort_basic():
    """Test basic sorting functionality"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == sorted(arr)

def test_cartesian_tree_sort_empty():
    """Test sorting an empty list"""
    arr = []
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == []

def test_cartesian_tree_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == [42]

def test_cartesian_tree_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == arr

def test_cartesian_tree_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == sorted(arr)

def test_cartesian_tree_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = cartesian_tree_sort(arr)
    assert sorted_arr == sorted(arr)

def test_build_cartesian_tree():
    """Test the Cartesian tree building process"""
    arr = [3, 1, 4, 1, 5]
    root = build_cartesian_tree(arr)
    
    # Verify the root is the minimum element
    assert root.value == 1
    
    # Verify left and right children of root
    assert root.right.value == 3
    assert root.right.right.value == 4
    assert root.right.right.right.value == 5