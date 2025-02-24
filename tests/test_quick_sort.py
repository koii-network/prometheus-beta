import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from quick_sort import quick_sort

def test_quick_sort_basic():
    """Test basic sorting functionality"""
    assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_quick_sort_empty_list():
    """Test sorting an empty list"""
    assert quick_sort([]) == []

def test_quick_sort_single_element():
    """Test sorting a single-element list"""
    assert quick_sort([42]) == [42]

def test_quick_sort_already_sorted():
    """Test sorting an already sorted list"""
    sorted_list = [1, 2, 3, 4, 5]
    assert quick_sort(sorted_list) == sorted_list

def test_quick_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_quick_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    assert quick_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]

def test_quick_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert quick_sort([-3, -1, -4, 0, 2, -2]) == [-4, -3, -2, -1, 0, 2]

def test_quick_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    assert quick_sort([-1, 5, 0, -4, 3, 10, -9]) == [-9, -4, -1, 0, 3, 5, 10]

def test_quick_sort_original_list_unchanged():
    """Verify that the original list remains unchanged"""
    original = [3, 1, 4, 1, 5]
    _ = quick_sort(original)
    assert original == [3, 1, 4, 1, 5]

def test_quick_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort("not a list")

def test_quick_sort_list_of_floats():
    """Test sorting a list of floating-point numbers"""
    assert quick_sort([3.14, 2.71, 1.41, 0.58]) == [0.58, 1.41, 2.71, 3.14]