import pytest
from src.library_sort import library_sort

def test_library_sort_basic():
    """Test basic sorting functionality"""
    assert library_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_library_sort_empty_list():
    """Test sorting an empty list"""
    assert library_sort([]) == []

def test_library_sort_single_element():
    """Test sorting a single-element list"""
    assert library_sort([42]) == [42]

def test_library_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert library_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_library_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert library_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_library_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    assert library_sort([3, 3, 2, 1, 3]) == [1, 2, 3, 3, 3]

def test_library_sort_invalid_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        library_sort("not a list")

def test_library_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert library_sort([-3, -1, -4, 0, 2, -2]) == [-4, -3, -2, -1, 0, 2]

def test_library_sort_mixed_types_numbers():
    """Test sorting a list with mixed number types"""
    assert library_sort([1.5, 1, 2, -3.5, 0]) == [-3.5, 0, 1, 1.5, 2]