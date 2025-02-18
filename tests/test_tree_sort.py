import pytest
from src.tree_sort import tree_sort

def test_tree_sort_normal_list():
    """Test sorting a normal list of integers."""
    input_list = [5, 2, 9, 1, 7, 6, 3]
    assert tree_sort(input_list) == [1, 2, 3, 5, 6, 7, 9]

def test_tree_sort_empty_list():
    """Test sorting an empty list."""
    assert tree_sort([]) == []

def test_tree_sort_single_element():
    """Test sorting a list with a single element."""
    assert tree_sort([42]) == [42]

def test_tree_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert tree_sort(input_list) == [1, 2, 3, 4, 5]

def test_tree_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    assert tree_sort(input_list) == [1, 2, 3, 4, 5]

def test_tree_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert tree_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_tree_sort_floating_point():
    """Test sorting a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    assert tree_sort(input_list) == [0.58, 1.41, 2.71, 3.14]

def test_tree_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        tree_sort("not a list")
        tree_sort(123)
        tree_sort(None)

def test_tree_sort_incomparable_elements():
    """Test that ValueError is raised for incomparable elements."""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        tree_sort([1, "a", 3])
        tree_sort([object(), 2, 3])