import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from heap_sort import heap_sort

def test_heap_sort_normal_list():
    """Test heap sort with a normal list of integers"""
    arr = [12, 11, 13, 5, 6, 7]
    assert heap_sort(arr) == [5, 6, 7, 11, 12, 13]

def test_heap_sort_already_sorted():
    """Test heap sort with an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert heap_sort(arr) == [1, 2, 3, 4, 5]

def test_heap_sort_reverse_sorted():
    """Test heap sort with a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert heap_sort(arr) == [1, 2, 3, 4, 5]

def test_heap_sort_with_duplicates():
    """Test heap sort with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert heap_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_heap_sort_empty_list():
    """Test heap sort with an empty list"""
    arr = []
    assert heap_sort(arr) == []

def test_heap_sort_single_element():
    """Test heap sort with a single element"""
    arr = [42]
    assert heap_sort(arr) == [42]

def test_heap_sort_float_numbers():
    """Test heap sort with floating point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert heap_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_heap_sort_with_negative_numbers():
    """Test heap sort with negative numbers"""
    arr = [-4, 1, -9, 0, 5, -2]
    assert heap_sort(arr) == [-9, -4, -2, 0, 1, 5]

def test_heap_sort_non_list_input():
    """Test heap sort with non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        heap_sort("not a list")

def test_heap_sort_non_comparable_elements():
    """Test heap sort with non-comparable elements"""
    with pytest.raises(ValueError, match="List contains non-comparable elements"):
        heap_sort([1, 2, [3], 4])

def test_heap_sort_original_list_unchanged():
    """Test that the original list remains unchanged"""
    original = [5, 2, 9, 1, 7]
    _ = heap_sort(original)
    assert original == [5, 2, 9, 1, 7]