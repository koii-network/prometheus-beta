import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from tree_sort import tree_sort

def test_tree_sort_basic():
    """Test basic sorting of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert tree_sort(input_list) == sorted(input_list)

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
    assert tree_sort(input_list) == sorted(input_list)

def test_tree_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert tree_sort(input_list) == sorted(input_list)

def test_tree_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert tree_sort(input_list) == sorted(input_list)

def test_tree_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 2, -10, 0, 7, -3]
    assert tree_sort(input_list) == sorted(input_list)

def test_tree_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        tree_sort("not a list")

def test_tree_sort_incomparable_elements():
    """Test that a ValueError is raised for incomparable elements"""
    with pytest.raises(ValueError):
        tree_sort([1, 2, "a"])