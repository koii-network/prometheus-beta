import pytest
from src.gnome_sort import gnome_sort

def test_gnome_sort_normal_list():
    """Test sorting a normal list of numbers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert gnome_sort(input_list) == expected

def test_gnome_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert gnome_sort(input_list) == input_list

def test_gnome_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
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

def test_gnome_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert gnome_sort(input_list) == expected

def test_gnome_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, -2, -8, -1, -9]
    expected = sorted(input_list)
    assert gnome_sort(input_list) == expected

def test_gnome_sort_floating_point():
    """Test sorting a list with floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert gnome_sort(input_list) == expected

def test_gnome_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        gnome_sort("not a list")

def test_gnome_sort_incomparable_elements():
    """Test handling of mixed or incomparable elements"""
    with pytest.raises(TypeError):
        gnome_sort([1, 'a', 2, 'b'])  # Cannot compare int and str