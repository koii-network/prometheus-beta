import pytest
from src.tree_sort import tree_sort

def test_tree_sort_basic_integers():
    """Test sorting a list of integers"""
    input_list = [5, 2, 9, 1, 7, 6, 3]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert tree_sort(input_list) == input_list

def test_tree_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_empty_list():
    """Test sorting an empty list"""
    assert tree_sort([]) == []

def test_tree_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert tree_sort(input_list) == input_list

def test_tree_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_floating_point():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_negative_numbers():
    """Test sorting a list of negative numbers"""
    input_list = [-5, -2, -9, -1, -7, -6, -3]
    expected = sorted(input_list)
    assert tree_sort(input_list) == expected

def test_tree_sort_invalid_input_type():
    """Test that a TypeError is raised for invalid input types"""
    with pytest.raises(TypeError):
        tree_sort("not a list")
    
    with pytest.raises(TypeError):
        tree_sort(123)
    
    with pytest.raises(TypeError):
        tree_sort(None)