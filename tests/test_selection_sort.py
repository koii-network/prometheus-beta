import pytest
from src.selection_sort import selection_sort

def test_selection_sort_basic():
    """Test basic sorting of integers"""
    assert selection_sort([5, 2, 9, 1, 7, 6]) == [1, 2, 5, 6, 7, 9]

def test_selection_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_selection_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_selection_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    assert selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_selection_sort_empty_list():
    """Test sorting an empty list"""
    assert selection_sort([]) == []

def test_selection_sort_single_element():
    """Test sorting a list with a single element"""
    assert selection_sort([42]) == [42]

def test_selection_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert selection_sort([-5, 2, -9, 1, 7, -6]) == [-9, -6, -5, 1, 2, 7]

def test_selection_sort_float_numbers():
    """Test sorting a list with floating-point numbers"""
    assert selection_sort([3.14, 2.71, 1.41, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_selection_sort_strings():
    """Test sorting a list of strings"""
    assert selection_sort(['banana', 'apple', 'cherry', 'date']) == ['apple', 'banana', 'cherry', 'date']

def test_selection_sort_non_list_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        selection_sort("not a list")

def test_selection_sort_non_comparable_elements():
    """Test that a TypeError is raised for non-comparable elements"""
    with pytest.raises(TypeError, match="List contains elements that cannot be compared"):
        selection_sort([1, 2, [3], 4])