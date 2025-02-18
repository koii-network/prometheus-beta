import pytest
from src.stooge_sort import stooge_sort

def test_stooge_sort_empty_list():
    """Test sorting an empty list."""
    assert stooge_sort([]) == []

def test_stooge_sort_single_element():
    """Test sorting a list with a single element."""
    assert stooge_sort([5]) == [5]

def test_stooge_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert stooge_sort(input_list) == [1, 2, 3, 4, 5]

def test_stooge_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    assert stooge_sort(input_list) == [1, 2, 3, 4, 5]

def test_stooge_sort_random_list():
    """Test sorting a random list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert stooge_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_stooge_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert stooge_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_stooge_sort_preserves_original_list():
    """Test that the original list is not modified."""
    input_list = [5, 2, 9, 1, 7]
    sorted_list = stooge_sort(input_list)
    assert input_list == [5, 2, 9, 1, 7]  # Original list should remain unchanged
    assert sorted_list == [1, 2, 5, 7, 9]  # Sorted list should be correct