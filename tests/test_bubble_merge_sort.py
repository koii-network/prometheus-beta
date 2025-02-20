import pytest
from src.bubble_merge_sort import bubble_merge_sort

def test_bubble_merge_sort_basic():
    """Test basic sorting functionality."""
    assert bubble_merge_sort([4, 2, 1, 3]) == [1, 2, 3, 4]

def test_bubble_merge_sort_already_sorted():
    """Test with an already sorted list."""
    assert bubble_merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_bubble_merge_sort_reverse_sorted():
    """Test with a reverse sorted list."""
    assert bubble_merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]

def test_bubble_merge_sort_empty_list():
    """Test with an empty list."""
    assert bubble_merge_sort([]) == []

def test_bubble_merge_sort_single_element():
    """Test with a single element list."""
    assert bubble_merge_sort([42]) == [42]

def test_bubble_merge_sort_duplicates():
    """Test with duplicate elements."""
    assert bubble_merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bubble_merge_sort_large_input():
    """Test with a larger input to verify complex sorting."""
    input_list = [29, 10, 14, 37, 18, 26, 54, 41, 33, 8]
    assert bubble_merge_sort(input_list) == sorted(input_list)

def test_bubble_merge_sort_negative_numbers():
    """Test sorting with negative numbers."""
    assert bubble_merge_sort([-4, 2, -1, 3, -5, 0]) == [-5, -4, -1, 0, 2, 3]