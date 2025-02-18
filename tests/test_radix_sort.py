import pytest
from src.radix_sort import radix_sort

def test_radix_sort_normal_case():
    """Test radix sort with a standard list of non-negative integers."""
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    assert radix_sort(arr) == [2, 24, 45, 66, 75, 90, 170, 802]

def test_radix_sort_empty_list():
    """Test radix sort with an empty list."""
    assert radix_sort([]) == []

def test_radix_sort_single_element():
    """Test radix sort with a single element."""
    assert radix_sort([42]) == [42]

def test_radix_sort_already_sorted():
    """Test radix sort with an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert radix_sort(arr) == [1, 2, 3, 4, 5]

def test_radix_sort_reverse_sorted():
    """Test radix sort with a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert radix_sort(arr) == [1, 2, 3, 4, 5]

def test_radix_sort_with_zeros():
    """Test radix sort with multiple zeros."""
    arr = [0, 0, 0, 5, 3, 0, 2]
    assert radix_sort(arr) == [0, 0, 0, 0, 2, 3, 5]

def test_radix_sort_negative_numbers():
    """Test that radix sort raises an error for negative numbers."""
    with pytest.raises(ValueError, match="Radix sort only works with non-negative integers"):
        radix_sort([1, 2, -3, 4])