import pytest
from src.quick_sort import quick_sort

def test_quick_sort_empty_list():
    """Test sorting an empty list"""
    assert quick_sort([]) == []

def test_quick_sort_single_element():
    """Test sorting a list with a single element"""
    assert quick_sort([5]) == [5]

def test_quick_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert quick_sort(input_list) == [1, 2, 3, 4, 5]

def test_quick_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert quick_sort(input_list) == [1, 2, 3, 4, 5]

def test_quick_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert quick_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_quick_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-3, 4, -1, 7, -5, 0, 2]
    assert quick_sort(input_list) == [-5, -3, -1, 0, 2, 4, 7]

def test_quick_sort_non_list_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort("not a list")

def test_quick_sort_preserves_original_list():
    """Test that the original list is not modified"""
    original_list = [3, 1, 4, 1, 5]
    quick_sort(original_list)
    assert original_list == [3, 1, 4, 1, 5]