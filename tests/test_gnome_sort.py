import pytest
from src.gnome_sort import gnome_sort

def test_gnome_sort_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert gnome_sort(input_list) == expected

def test_gnome_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert gnome_sort(input_list) == input_list

def test_gnome_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert gnome_sort(input_list) == expected

def test_gnome_sort_empty_list():
    """Test sorting an empty list"""
    assert gnome_sort([]) == []

def test_gnome_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert gnome_sort(input_list) == input_list

def test_gnome_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert gnome_sort(input_list) == expected

def test_gnome_sort_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        gnome_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        gnome_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        gnome_sort(None)

def test_gnome_sort_preserves_original_list():
    """Test that the original list is not modified"""
    input_list = [5, 2, 9, 1, 7]
    original_copy = input_list.copy()
    gnome_sort(input_list)
    assert input_list == original_copy