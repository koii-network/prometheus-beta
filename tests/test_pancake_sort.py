import pytest
from src.pancake_sort import pancake_sort

def test_pancake_sort_normal_list():
    """Test sorting a normal list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert pancake_sort(arr) == sorted(arr)

def test_pancake_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert pancake_sort(arr) == arr

def test_pancake_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert pancake_sort(arr) == sorted(arr)

def test_pancake_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert pancake_sort(arr) == []

def test_pancake_sort_single_element():
    """Test sorting a single-element list."""
    arr = [42]
    assert pancake_sort(arr) == [42]

def test_pancake_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert pancake_sort(arr) == sorted(arr)

def test_pancake_sort_input_type_error():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        pancake_sort("not a list")

def test_pancake_sort_preserves_original_list():
    """Test that the original list is not modified."""
    arr = [5, 2, 9, 1, 7]
    original = arr.copy()
    pancake_sort(arr)
    assert arr == original