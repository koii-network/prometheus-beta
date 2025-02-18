import pytest
from src.bead_sort import bead_sort

def test_bead_sort_basic():
    """Test basic sorting functionality"""
    assert bead_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_bead_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert bead_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bead_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert bead_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bead_sort_with_duplicates():
    """Test sorting a list with duplicate values"""
    assert bead_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_bead_sort_empty_list():
    """Test sorting an empty list"""
    assert bead_sort([]) == []

def test_bead_sort_single_element():
    """Test sorting a list with a single element"""
    assert bead_sort([42]) == [42]

def test_bead_sort_zero_values():
    """Test sorting a list with zero values"""
    assert bead_sort([0, 0, 0, 0]) == [0, 0, 0, 0]

def test_bead_sort_invalid_input_negative():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError):
        bead_sort([-1, 2, 3])

def test_bead_sort_invalid_input_non_integer():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError):
        bead_sort([1, 2, 'a'])

def test_bead_sort_invalid_input_not_list():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError):
        bead_sort("not a list")