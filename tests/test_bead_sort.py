import pytest
from src.bead_sort import bead_sort

def test_bead_sort_empty_list():
    """Test sorting an empty list"""
    assert bead_sort([]) == []

def test_bead_sort_single_element():
    """Test sorting a list with a single element"""
    assert bead_sort([5]) == [5]

def test_bead_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    assert bead_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bead_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    assert bead_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bead_sort_random_list():
    """Test sorting a random list of positive integers"""
    assert bead_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bead_sort_with_duplicates():
    """Test sorting a list with duplicate values"""
    assert bead_sort([2, 2, 1, 3, 1]) == [1, 1, 2, 2, 3]

def test_bead_sort_negative_numbers():
    """Test that a ValueError is raised when negative numbers are present"""
    with pytest.raises(ValueError, match="Bead sort only works with non-negative integers"):
        bead_sort([-1, 2, 3])

def test_bead_sort_zero_included():
    """Test sorting a list that includes zero"""
    assert bead_sort([3, 0, 2, 1]) == [0, 1, 2, 3]