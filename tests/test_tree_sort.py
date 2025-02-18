import pytest
from src.tree_sort import tree_sort

def test_tree_sort_basic():
    """Test sorting a list of integers."""
    arr = [5, 2, 9, 1, 7, 6]
    assert tree_sort(arr) == [1, 2, 5, 6, 7, 9]

def test_tree_sort_empty_list():
    """Test sorting an empty list."""
    assert tree_sort([]) == []

def test_tree_sort_single_element():
    """Test sorting a list with a single element."""
    assert tree_sort([42]) == [42]

def test_tree_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert tree_sort(arr) == [1, 2, 3, 4, 5]

def test_tree_sort_reverse_sorted():
    """Test sorting a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert tree_sort(arr) == [1, 2, 3, 4, 5]

def test_tree_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert tree_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_tree_sort_invalid_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        tree_sort("not a list")
        tree_sort(123)
        tree_sort(None)