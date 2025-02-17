import pytest
from src.merge_sort import merge_sort

def test_merge_sort_empty_list():
    """Test merge sort with an empty list."""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test merge sort with a single element."""
    assert merge_sort([42]) == [42]

def test_merge_sort_already_sorted():
    """Test merge sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert merge_sort(input_list) == input_list

def test_merge_sort_reverse_sorted():
    """Test merge sort with a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    assert merge_sort(input_list) == [1, 2, 3, 4, 5]

def test_merge_sort_random_list():
    """Test merge sort with a random unsorted list."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert merge_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_merge_sort_with_duplicates():
    """Test merge sort with a list containing duplicate elements."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert merge_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_merge_sort_raises_type_error():
    """Test that merge sort raises a TypeError for non-list inputs."""
    with pytest.raises(TypeError):
        merge_sort("not a list")
    with pytest.raises(TypeError):
        merge_sort(123)
    with pytest.raises(TypeError):
        merge_sort(None)