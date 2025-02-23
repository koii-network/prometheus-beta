import pytest
from src.merge_sort import merge_sort

def test_merge_sort_basic():
    """Test basic sorting of a list of integers."""
    arr = [5, 2, 9, 1, 7, 6]
    assert merge_sort(arr) == [1, 2, 5, 6, 7, 9]

def test_merge_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert merge_sort(arr) == []

def test_merge_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert merge_sort(arr) == [42]

def test_merge_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]

def test_merge_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]

def test_merge_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert merge_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_merge_sort_with_floats():
    """Test sorting a list of floating-point numbers."""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert merge_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_merge_sort_with_strings():
    """Test sorting a list of strings."""
    arr = ["banana", "apple", "cherry", "date"]
    assert merge_sort(arr) == ["apple", "banana", "cherry", "date"]

def test_merge_sort_input_type_error():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort("not a list")

def test_merge_sort_preserves_original():
    """Test that the original list is not modified."""
    original = [5, 2, 9, 1, 7, 6]
    result = merge_sort(original)
    assert result == [1, 2, 5, 6, 7, 9]
    assert original == [5, 2, 9, 1, 7, 6]  # Original list unchanged