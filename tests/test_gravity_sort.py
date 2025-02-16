import pytest
from src.gravity_sort import gravity_sort

def test_gravity_sort_basic():
    """Test basic sorting functionality."""
    assert gravity_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_gravity_sort_already_sorted():
    """Test when the list is already sorted."""
    assert gravity_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_gravity_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    assert gravity_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_gravity_sort_with_duplicates():
    """Test sorting a list with duplicate values."""
    assert gravity_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_gravity_sort_empty_list():
    """Test sorting an empty list."""
    assert gravity_sort([]) == []

def test_gravity_sort_single_element():
    """Test sorting a list with a single element."""
    assert gravity_sort([42]) == [42]

def test_gravity_sort_negative_numbers():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Gravity sort only works with non-negative integers"):
        gravity_sort([-1, 2, 3])

def test_gravity_sort_zero_and_positive():
    """Test sorting a list with zero and positive numbers."""
    assert gravity_sort([0, 3, 1, 0, 5]) == [0, 0, 1, 3, 5]