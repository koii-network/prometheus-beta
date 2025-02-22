import pytest
from src.sorting import quick_sort

def test_quick_sort_normal_case():
    """Test sorting a typical list of integers"""
    input_list = [3, 6, 1, 8, 2, 5]
    expected = [1, 2, 3, 5, 6, 8]
    assert quick_sort(input_list) == expected

def test_quick_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert quick_sort(input_list) == input_list

def test_quick_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert quick_sort(input_list) == expected

def test_quick_sort_empty_list():
    """Test sorting an empty list"""
    assert quick_sort([]) == []

def test_quick_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert quick_sort(input_list) == input_list

def test_quick_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    assert quick_sort(input_list) == expected

def test_quick_sort_invalid_input_non_list():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort("not a list")

def test_quick_sort_invalid_input_non_integers():
    """Test that TypeError is raised for list with non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        quick_sort([1, 2, "3", 4])