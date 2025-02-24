import pytest
from src.merge_sort import merge_sort

def test_merge_sort_empty_list():
    """Test sorting an empty list."""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test sorting a list with a single element."""
    assert merge_sort([5]) == [5]

def test_merge_sort_numeric_list():
    """Test sorting a list of numbers."""
    assert merge_sort([5, 2, 9, 1, 7, 6, 3]) == [1, 2, 3, 5, 6, 7, 9]

def test_merge_sort_already_sorted():
    """Test sorting an already sorted list."""
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_merge_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_merge_sort_floating_point():
    """Test sorting a list of floating-point numbers."""
    assert merge_sort([3.14, 2.71, 1.41, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_merge_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    assert merge_sort([-5, -2, -9, -1, -7]) == [-9, -7, -5, -2, -1]

def test_merge_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers."""
    assert merge_sort([-5, 2, 0, -3, 7, 1]) == [-5, -3, 0, 1, 2, 7]

def test_merge_sort_non_list_input():
    """Test error handling for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort("not a list")

def test_merge_sort_uncomparable_elements():
    """Test error handling for uncomparable elements."""
    with pytest.raises(TypeError, match="List contains elements that cannot be compared"):
        merge_sort([1, 2, "a"])