import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from tree_sort import tree_sort

def test_tree_sort_basic():
    """Test sorting a list of integers"""
    input_list = [5, 2, 9, 1, 7, 6, 3]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_empty_list():
    """Test sorting an empty list"""
    assert tree_sort([]) == []

def test_tree_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert tree_sort(input_list) == [42]

def test_tree_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert tree_sort(input_list) == input_list

def test_tree_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [5, 2, 5, 1, 2, 3]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_floating_point():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_strings():
    """Test sorting a list of strings"""
    input_list = ["banana", "apple", "cherry", "date"]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        tree_sort("not a list")
    with pytest.raises(TypeError):
        tree_sort(123)

def test_tree_sort_non_comparable_elements():
    """Test that a ValueError is raised for non-comparable elements"""
    class UncomparableClass:
        pass
    
    with pytest.raises(ValueError):
        tree_sort([1, UncomparableClass(), 3])