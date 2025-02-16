import pytest
from src.gnome_sort import gnome_sort

def test_gnome_sort_basic():
    """Test basic sorting functionality"""
    assert gnome_sort([5, 2, 9, 1, 7, 6]) == [1, 2, 5, 6, 7, 9]

def test_gnome_sort_already_sorted():
    """Test list that is already sorted"""
    assert gnome_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_gnome_sort_reverse_sorted():
    """Test list in reverse order"""
    assert gnome_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_gnome_sort_duplicates():
    """Test list with duplicate elements"""
    assert gnome_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_gnome_sort_empty_list():
    """Test empty list"""
    assert gnome_sort([]) == []

def test_gnome_sort_single_element():
    """Test list with single element"""
    assert gnome_sort([42]) == [42]

def test_gnome_sort_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        gnome_sort("not a list")
    with pytest.raises(TypeError):
        gnome_sort(123)
    with pytest.raises(TypeError):
        gnome_sort(None)