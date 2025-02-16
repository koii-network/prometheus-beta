import pytest
from src.tree_sort import tree_sort

def test_tree_sort_basic():
    """
    Test tree sort with a basic list of integers
    """
    input_list = [5, 2, 9, 1, 7, 6]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_empty_list():
    """
    Test tree sort with an empty list
    """
    assert tree_sort([]) == []

def test_tree_sort_single_element():
    """
    Test tree sort with a single element
    """
    input_list = [42]
    assert tree_sort(input_list) == [42]

def test_tree_sort_already_sorted():
    """
    Test tree sort with an already sorted list
    """
    input_list = [1, 2, 3, 4, 5]
    assert tree_sort(input_list) == input_list

def test_tree_sort_reverse_sorted():
    """
    Test tree sort with a reverse sorted list
    """
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_with_duplicates():
    """
    Test tree sort with duplicate elements
    """
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_with_floats():
    """
    Test tree sort with floating-point numbers
    """
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_with_strings():
    """
    Test tree sort with strings
    """
    input_list = ['banana', 'apple', 'cherry', 'date']
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_invalid_input_type():
    """
    Test tree sort with invalid input type
    """
    with pytest.raises(TypeError):
        tree_sort("not a list")
    with pytest.raises(TypeError):
        tree_sort(123)

def test_tree_sort_uncomparable_elements():
    """
    Test tree sort with elements that cannot be compared
    """
    with pytest.raises(ValueError):
        tree_sort([1, 2, [3], 4])