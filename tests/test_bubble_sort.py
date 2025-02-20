import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_basic():
    """Test basic sorting functionality."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_sort(arr) == sorted(arr)

def test_bubble_sort_already_sorted():
    """Test when the list is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert bubble_sort(arr) == arr

def test_bubble_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert bubble_sort(arr) == sorted(arr)

def test_bubble_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bubble_sort(arr) == sorted(arr)

def test_bubble_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert bubble_sort(arr) == []

def test_bubble_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert bubble_sort(arr) == [42]

def test_bubble_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-1, -5, 10, -3, 0, 8]
    assert bubble_sort(arr) == sorted(arr)

def test_bubble_sort_original_list_unchanged():
    """Ensure the original list is not modified."""
    arr = [5, 2, 9, 1, 7]
    original = arr.copy()
    bubble_sort(arr)
    assert arr == original