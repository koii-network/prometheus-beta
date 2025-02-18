import pytest
from src.gnome_sort import gnome_sort

def test_gnome_sort_basic():
    """Test basic sorting functionality"""
    assert gnome_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_gnome_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert gnome_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_gnome_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    assert gnome_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_gnome_sort_empty_list():
    """Test sorting an empty list"""
    assert gnome_sort([]) == []

def test_gnome_sort_single_element():
    """Test sorting a list with a single element"""
    assert gnome_sort([42]) == [42]

def test_gnome_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    assert gnome_sort([3, 3, 1, 4, 1, 5, 9, 2, 6, 2]) == [1, 1, 2, 2, 3, 3, 4, 5, 6, 9]

def test_gnome_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert gnome_sort([-3, 1, -5, 0, 4, -1]) == [-5, -3, -1, 0, 1, 4]

def test_gnome_sort_invalid_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        gnome_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        gnome_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        gnome_sort(None)