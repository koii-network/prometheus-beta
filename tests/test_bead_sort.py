import pytest
from src.bead_sort import bead_sort

def test_bead_sort_basic():
    """Test basic sorting functionality"""
    assert bead_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_bead_sort_already_sorted():
    """Test when input is already sorted"""
    assert bead_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bead_sort_reverse_sorted():
    """Test when input is in reverse order"""
    assert bead_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bead_sort_duplicates():
    """Test sorting with duplicate values"""
    assert bead_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_bead_sort_empty_list():
    """Test sorting an empty list"""
    assert bead_sort([]) == []

def test_bead_sort_single_element():
    """Test sorting a single-element list"""
    assert bead_sort([42]) == [42]

def test_bead_sort_all_same():
    """Test sorting a list with all same elements"""
    assert bead_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

def test_bead_sort_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="Bead sort only works with non-negative integers"):
        bead_sort([-1, 2, 3])

def test_bead_sort_large_numbers():
    """Test sorting with larger numbers"""
    input_list = [1000, 10, 100, 1, 10000]
    assert bead_sort(input_list) == [1, 10, 100, 1000, 10000]