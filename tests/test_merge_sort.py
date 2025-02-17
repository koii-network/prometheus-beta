import pytest
from src.merge_sort import merge_sort

def test_merge_sort_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert merge_sort(input_list) == expected

def test_merge_sort_empty_list():
    """Test sorting an empty list"""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test sorting a list with a single element"""
    single_element_list = [42]
    assert merge_sort(single_element_list) == single_element_list

def test_merge_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    sorted_list = [1, 2, 3, 4, 5]
    assert merge_sort(sorted_list) == sorted_list

def test_merge_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    reverse_sorted = [5, 4, 3, 2, 1]
    expected = sorted(reverse_sorted)
    assert merge_sort(reverse_sorted) == expected

def test_merge_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    list_with_duplicates = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(list_with_duplicates)
    assert merge_sort(list_with_duplicates) == expected

def test_merge_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    float_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    expected = sorted(float_list)
    assert merge_sort(float_list) == expected

def test_merge_sort_invalid_input():
    """Test that an error is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort("not a list")

def test_merge_sort_preserves_original():
    """Test that the original list is not modified"""
    original = [5, 2, 9, 1, 7]
    merge_sort(original)
    assert original == [5, 2, 9, 1, 7]  # Original list should remain unchanged