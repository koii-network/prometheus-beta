import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bead_sort import bead_sort

def test_bead_sort_basic():
    """Test basic sorting functionality"""
    assert bead_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_bead_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert bead_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bead_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert bead_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bead_sort_duplicates():
    """Test sorting a list with duplicate values"""
    assert bead_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_bead_sort_single_element():
    """Test sorting a single-element list"""
    assert bead_sort([42]) == [42]

def test_bead_sort_empty_list():
    """Test sorting an empty list"""
    assert bead_sort([]) == []

def test_bead_sort_zero_values():
    """Test sorting a list with zero values"""
    assert bead_sort([0, 0, 0, 0]) == [0, 0, 0, 0]

def test_bead_sort_invalid_input_negative():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="Input must be a list of non-negative integers"):
        bead_sort([-1, 2, 3])

def test_bead_sort_invalid_input_type():
    """Test that non-integer inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Input must be a list of non-negative integers"):
        bead_sort([1, 2, 'three'])

def test_bead_sort_non_list_input():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        bead_sort("not a list")