import pytest
from src.bead_sort import bead_sort

def test_bead_sort_normal_case():
    """Test bead sort with a typical unsorted list of positive integers."""
    assert bead_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_bead_sort_already_sorted():
    """Test bead sort with an already sorted list."""
    assert bead_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bead_sort_reverse_sorted():
    """Test bead sort with a reverse-sorted list."""
    assert bead_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bead_sort_with_duplicates():
    """Test bead sort with a list containing duplicate values."""
    assert bead_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_bead_sort_empty_list():
    """Test bead sort with an empty list."""
    assert bead_sort([]) == []

def test_bead_sort_single_element():
    """Test bead sort with a single-element list."""
    assert bead_sort([42]) == [42]

def test_bead_sort_invalid_input_negative():
    """Test that bead sort raises an error for negative numbers."""
    with pytest.raises(ValueError, match="Bead sort only works with non-negative integers"):
        bead_sort([-1, 2, 3])

def test_bead_sort_invalid_input_float():
    """Test that bead sort raises an error for non-integer inputs."""
    with pytest.raises(ValueError, match="Bead sort only works with non-negative integers"):
        bead_sort([1.5, 2, 3])

def test_bead_sort_large_numbers():
    """Test bead sort with larger numbers."""
    assert bead_sort([1000, 10, 100, 1]) == [1, 10, 100, 1000]