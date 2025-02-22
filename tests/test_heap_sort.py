import pytest
from src.heap_sort import heap_sort

def test_heap_sort_basic():
    """Test basic sorting of a list of integers."""
    arr = [12, 11, 13, 5, 6, 7]
    assert heap_sort(arr) == [5, 6, 7, 11, 12, 13]

def test_heap_sort_empty_list():
    """Test sorting an empty list."""
    assert heap_sort([]) == []

def test_heap_sort_single_element():
    """Test sorting a list with a single element."""
    assert heap_sort([42]) == [42]

def test_heap_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert heap_sort(arr) == [1, 2, 3, 4, 5]

def test_heap_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    assert heap_sort(arr) == [1, 2, 3, 4, 5]

def test_heap_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert heap_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_heap_sort_float_numbers():
    """Test sorting a list of floating-point numbers."""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert heap_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_heap_sort_invalid_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        heap_sort("not a list")

def test_heap_sort_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-1, -5, 10, 0, -3, 8]
    assert heap_sort(arr) == [-5, -3, -1, 0, 8, 10]