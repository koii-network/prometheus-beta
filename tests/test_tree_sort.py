import pytest
from src.tree_sort import tree_sort

def test_tree_sort_empty_list():
    """Test sorting an empty list"""
    assert tree_sort([]) == []

def test_tree_sort_single_element():
    """Test sorting a list with a single element"""
    assert tree_sort([5]) == [5]

def test_tree_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    assert tree_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_tree_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    assert tree_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_tree_sort_unsorted_list():
    """Test sorting an unsorted list"""
    assert tree_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_tree_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert tree_sort([-5, 3, 0, -2, 7]) == [-5, -2, 0, 3, 7]

def test_tree_sort_with_duplicate_numbers():
    """Test sorting a list with duplicate numbers"""
    assert tree_sort([3, 3, 1, 1, 2, 2]) == [1, 1, 2, 2, 3, 3]

def test_tree_sort_invalid_input():
    """Test that tree_sort raises TypeError for non-list input"""
    with pytest.raises(TypeError):
        tree_sort("not a list")
    with pytest.raises(TypeError):
        tree_sort(42)
    with pytest.raises(TypeError):
        tree_sort(None)