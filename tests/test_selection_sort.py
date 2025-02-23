import pytest
from src.selection_sort import selection_sort

def test_selection_sort_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert selection_sort(input_list) == expected

def test_selection_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert selection_sort(input_list) == input_list

def test_selection_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert selection_sort(input_list) == expected

def test_selection_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = [1, 2, 2, 3, 3, 4, 8]
    assert selection_sort(input_list) == expected

def test_selection_sort_empty_list():
    """Test sorting an empty list"""
    assert selection_sort([]) == []

def test_selection_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert selection_sort(input_list) == [42]

def test_selection_sort_floats():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert selection_sort(input_list) == expected

def test_selection_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 0, 10, -3, 7]
    expected = [-5, -3, 0, 7, 10]
    assert selection_sort(input_list) == expected

def test_selection_sort_non_list_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        selection_sort("not a list")

def test_selection_sort_non_comparable_elements():
    """Test that a TypeError is raised for non-comparable elements"""
    with pytest.raises(TypeError, match="List contains elements that cannot be compared"):
        selection_sort([1, 2, "3", 4])

def test_selection_sort_preserves_original():
    """Test that the original list is not modified"""
    original = [5, 2, 9, 1, 7]
    selection_sort(original)
    assert original == [5, 2, 9, 1, 7]