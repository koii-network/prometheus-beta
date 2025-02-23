import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from heap_sort import heap_sort

def test_heap_sort_normal_list():
    """Test heap sort with a normal list of integers."""
    arr = [12, 11, 13, 5, 6, 7]
    assert heap_sort(arr) == [5, 6, 7, 11, 12, 13]

def test_heap_sort_reverse_sorted():
    """Test heap sort with a reverse-sorted list."""
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert heap_sort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_heap_sort_already_sorted():
    """Test heap sort with an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert heap_sort(arr) == [1, 2, 3, 4, 5]

def test_heap_sort_single_element():
    """Test heap sort with a single-element list."""
    arr = [42]
    assert heap_sort(arr) == [42]

def test_heap_sort_empty_list():
    """Test heap sort with an empty list."""
    arr = []
    assert heap_sort(arr) == []

def test_heap_sort_with_duplicates():
    """Test heap sort with a list containing duplicate elements."""
    arr = [4, 2, 4, 1, 3, 2]
    assert heap_sort(arr) == [1, 2, 2, 3, 4, 4]

def test_heap_sort_with_negative_numbers():
    """Test heap sort with negative numbers."""
    arr = [-1, -5, 10, 0, -3, 8]
    assert heap_sort(arr) == [-5, -3, -1, 0, 8, 10]

def test_heap_sort_input_not_list():
    """Test that a TypeError is raised when input is not a list."""
    with pytest.raises(TypeError, match="Input must be a list"):
        heap_sort("not a list")

def test_heap_sort_preserves_original_list():
    """Test that the original list is not modified."""
    original = [5, 2, 9, 1, 7]
    heap_sort(original)
    assert original == [5, 2, 9, 1, 7]