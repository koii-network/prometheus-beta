import pytest
from src.tree_sort import tree_sort

def test_tree_sort_basic_integers():
    """Test sorting a list of integers"""
    input_list = [5, 2, 9, 1, 7]
    expected = [1, 2, 5, 7, 9]
    assert tree_sort(input_list) == expected

def test_tree_sort_empty_list():
    """Test sorting an empty list"""
    assert tree_sort([]) == []

def test_tree_sort_single_element():
    """Test sorting a list with a single element"""
    assert tree_sort([42]) == [42]

def test_tree_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert tree_sort(input_list) == input_list

def test_tree_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert tree_sort(input_list) == expected

def test_tree_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert tree_sort(input_list) == expected

def test_tree_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert tree_sort(input_list) == expected

def test_tree_sort_with_strings():
    """Test sorting a list of strings"""
    input_list = ['banana', 'apple', 'cherry', 'date']
    expected = ['apple', 'banana', 'cherry', 'date']
    assert tree_sort(input_list) == expected

def test_tree_sort_invalid_input():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        tree_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        tree_sort(123)

def test_tree_sort_uncomparable_elements():
    """Test that a ValueError is raised for uncomparable elements"""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        tree_sort([1, 2, "string", 3])
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        tree_sort([1, 2, None, 3])