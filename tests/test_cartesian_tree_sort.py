import pytest
from src.cartesian_tree_sort import cartesian_tree_sort, build_cartesian_tree, inorder_traversal

def test_cartesian_tree_sort_basic():
    """Test basic sorting functionality"""
    arr = [5, 2, 9, 1, 7]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_empty():
    """Test sorting an empty list"""
    assert cartesian_tree_sort([]) == []

def test_cartesian_tree_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert cartesian_tree_sort(arr) == [42]

def test_cartesian_tree_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    arr = [3, 3, 1, 4, 1, 5, 9, 2, 6]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert cartesian_tree_sort(arr) == arr

def test_cartesian_tree_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 2, -9, 1, 7]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_build_cartesian_tree():
    """Test the Cartesian tree building process"""
    arr = [5, 2, 9, 1, 7]
    tree_root = build_cartesian_tree(arr)
    
    # Validate the tree's structure
    assert tree_root.value == 9  # max value becomes root
    assert tree_root.left.value == 5
    assert tree_root.right.value == 7

def test_inorder_traversal():
    """Test in-order traversal of the Cartesian tree"""
    arr = [5, 2, 9, 1, 7]
    tree_root = build_cartesian_tree(arr)
    assert inorder_traversal(tree_root) == [1, 2, 5, 7, 9]