import pytest
from src.intro_sort import intro_sort

def test_intro_sort_empty_list():
    """Test sorting an empty list."""
    assert intro_sort([]) == []

def test_intro_sort_single_element():
    """Test sorting a list with a single element."""
    assert intro_sort([5]) == [5]

def test_intro_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert intro_sort(arr) == [1, 2, 3, 4, 5]

def test_intro_sort_reverse_sorted():
    """Test sorting a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert intro_sort(arr) == [1, 2, 3, 4, 5]

def test_intro_sort_random_list():
    """Test sorting a list with random elements."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert intro_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_intro_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert intro_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_intro_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-5, 10, -3, 0, 7, -1]
    assert intro_sort(arr) == [-5, -3, -1, 0, 7, 10]

def test_intro_sort_large_list():
    """Test sorting a larger list."""
    arr = list(range(100, 0, -1))
    assert intro_sort(arr) == list(range(1, 101))

def test_intro_sort_preserves_original_list():
    """Ensure the original list is not modified."""
    arr = [5, 2, 9, 1, 7]
    sorted_arr = intro_sort(arr)
    assert arr == [5, 2, 9, 1, 7]
    assert sorted_arr == [1, 2, 5, 7, 9]