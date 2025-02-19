import pytest
from src.sorting import merge_sort

def test_merge_sort_basic():
    """Test basic sorting of a random list of integers."""
    arr = [5, 2, 9, 1, 7, 6]
    assert merge_sort(arr) == [1, 2, 5, 6, 7, 9]

def test_merge_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]

def test_merge_sort_reverse_sorted():
    """Test sorting a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]

def test_merge_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert merge_sort(arr) == []

def test_merge_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert merge_sort(arr) == [42]

def test_merge_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert merge_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_merge_sort_input_type_error():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort("not a list")

def test_merge_sort_value_error():
    """Test that ValueError is raised for non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be integers"):
        merge_sort([1, 2, "3", 4])