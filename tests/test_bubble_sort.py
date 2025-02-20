import pytest
from src.bubble_sort import optimized_bubble_sort

def test_optimized_bubble_sort_normal_case():
    """Test sorting a standard list of numbers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_optimized_bubble_sort_already_sorted():
    """Test when list is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert optimized_bubble_sort(input_list) == input_list

def test_optimized_bubble_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_optimized_bubble_sort_empty_list():
    """Test sorting an empty list"""
    assert optimized_bubble_sort([]) == []

def test_optimized_bubble_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert optimized_bubble_sort(input_list) == input_list

def test_optimized_bubble_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_optimized_bubble_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        optimized_bubble_sort("not a list")
        optimized_bubble_sort(123)
        optimized_bubble_sort(None)