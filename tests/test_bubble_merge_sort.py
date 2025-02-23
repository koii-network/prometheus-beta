import pytest
from src.bubble_merge_sort import bubble_merge_sort

def test_bubble_merge_sort_empty_list():
    """Test sorting an empty list."""
    assert bubble_merge_sort([]) == []

def test_bubble_merge_sort_single_element():
    """Test sorting a list with a single element."""
    assert bubble_merge_sort([42]) == [42]

def test_bubble_merge_sort_already_sorted():
    """Test sorting an already sorted list."""
    sorted_list = [1, 2, 3, 4, 5]
    assert bubble_merge_sort(sorted_list) == sorted_list

def test_bubble_merge_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    assert bubble_merge_sort(input_list) == [1, 2, 3, 4, 5]

def test_bubble_merge_sort_random_list():
    """Test sorting a random unsorted list."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_merge_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_bubble_merge_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert bubble_merge_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_bubble_merge_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 0, 3, -2, 7, -1]
    assert bubble_merge_sort(input_list) == [-5, -2, -1, 0, 3, 7]

def test_bubble_merge_sort_large_list():
    """Test sorting a larger list."""
    import random
    random.seed(42)  # for reproducibility
    input_list = random.sample(range(1000), 100)
    assert bubble_merge_sort(input_list) == sorted(input_list)