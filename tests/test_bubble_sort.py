import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_normal_case():
    """Test sorting a typical unsorted list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == input_list

def test_bubble_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_with_duplicates():
    """Test sorting a list with duplicate values"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_empty_list():
    """Test sorting an empty list"""
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert bubble_sort(input_list) == input_list

def test_bubble_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        bubble_sort(42)

def test_bubble_sort_invalid_element_type():
    """Test that a TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        bubble_sort([1, 2, "three", 4])