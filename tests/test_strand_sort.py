import pytest
from src.strand_sort import strand_sort

def test_strand_sort_empty_list():
    """Test sorting an empty list."""
    assert strand_sort([]) == []

def test_strand_sort_single_element():
    """Test sorting a list with a single element."""
    assert strand_sort([5]) == [5]

def test_strand_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert strand_sort(arr) == [1, 2, 3, 4, 5]

def test_strand_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    assert strand_sort(arr) == [1, 2, 3, 4, 5]

def test_strand_sort_random_order():
    """Test sorting a list in random order."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert strand_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_strand_sort_with_duplicates():
    """Test sorting a list with duplicate values."""
    arr = [3, 3, 3, 1, 2, 2, 1]
    assert strand_sort(arr) == [1, 1, 2, 2, 3, 3, 3]

def test_strand_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-4, 1, -9, 0, 5, -2]
    assert strand_sort(arr) == [-9, -4, -2, 0, 1, 5]