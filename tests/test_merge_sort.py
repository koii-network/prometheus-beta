import pytest
from src.merge_sort import merge_sort

def test_merge_sort_empty_list():
    """Test merge sort with an empty list."""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test merge sort with a single element list."""
    assert merge_sort([5]) == [5]

def test_merge_sort_already_sorted():
    """Test merge sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert merge_sort(input_list) == input_list

def test_merge_sort_reverse_sorted():
    """Test merge sort with a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    assert merge_sort(input_list) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted_list():
    """Test merge sort with an unsorted list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert merge_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_merge_sort_with_duplicates():
    """Test merge sort with a list containing duplicate elements."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert merge_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_merge_sort_with_float_numbers():
    """Test merge sort with floating point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    assert merge_sort(input_list) == [0.58, 1.41, 2.71, 3.14]

def test_merge_sort_non_list_input():
    """Test merge sort with non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort("not a list")

def test_merge_sort_preserves_original_list():
    """Test that the original list is not modified."""
    input_list = [5, 2, 9, 1, 7]
    original_list = input_list.copy()
    merge_sort(input_list)
    assert input_list == original_list