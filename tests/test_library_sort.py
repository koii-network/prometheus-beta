import pytest
import sys
sys.path.append('.')  # Add project root to path

from src.library_sort import library_sort

def test_library_sort_basic():
    """Test basic sorting functionality"""
    arr = [5, 2, 9, 1, 7, 6]
    assert library_sort(arr) == [1, 2, 5, 6, 7, 9]

def test_library_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert library_sort(arr) == [1, 2, 3, 4, 5]

def test_library_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert library_sort(arr) == [1, 2, 3, 4, 5]

def test_library_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert library_sort(arr) == []

def test_library_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert library_sort(arr) == [42]

def test_library_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert library_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_library_sort_float_elements():
    """Test sorting a list with float elements"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert library_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_library_sort_invalid_input():
    """Test that an error is raised for non-list input"""
    with pytest.raises(TypeError):
        library_sort("not a list")

def test_library_sort_non_comparable():
    """Test handling of lists with non-comparable elements"""
    with pytest.raises(TypeError):
        library_sort([1, 2, "a", {}, 3])