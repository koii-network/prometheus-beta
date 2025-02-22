import pytest
from src.tree_sort import tree_sort

def test_tree_sort_basic():
    """Test basic sorting functionality"""
    arr = [5, 2, 9, 1, 7]
    assert tree_sort(arr) == [1, 2, 5, 7, 9]

def test_tree_sort_empty_list():
    """Test sorting an empty list"""
    assert tree_sort([]) == []

def test_tree_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert tree_sort(arr) == [1, 2, 3, 4, 5]

def test_tree_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert tree_sort(arr) == [1, 2, 3, 4, 5]

def test_tree_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert tree_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_tree_sort_with_floats():
    """Test sorting a list with floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert tree_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_tree_sort_invalid_input_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        tree_sort("not a list")

def test_tree_sort_incomparable_elements():
    """Test handling of incomparable elements"""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        tree_sort([1, "a", 3])