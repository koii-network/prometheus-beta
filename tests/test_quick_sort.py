import pytest
from src.quick_sort import quick_sort

def test_quick_sort_basic():
    """Test sorting a basic list of integers."""
    arr = [3, 6, 8, 10, 1, 2, 1]
    assert quick_sort(arr) == [1, 1, 2, 3, 6, 8, 10]

def test_quick_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert quick_sort(arr) == [1, 2, 3, 4, 5]

def test_quick_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert quick_sort(arr) == [1, 2, 3, 4, 5]

def test_quick_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert quick_sort(arr) == []

def test_quick_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert quick_sort(arr) == [42]

def test_quick_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 3, 3, 1, 1, 2]
    assert quick_sort(arr) == [1, 1, 2, 3, 3, 3]

def test_quick_sort_with_floats():
    """Test sorting a list of floating-point numbers."""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert quick_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_quick_sort_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-3, 0, 5, -1, 10, -5]
    assert quick_sort(arr) == [-5, -3, -1, 0, 5, 10]

def test_quick_sort_original_list_unchanged():
    """Test that the original list remains unchanged."""
    arr = [3, 1, 4, 1, 5, 9]
    original = arr.copy()
    quick_sort(arr)
    assert arr == original

def test_quick_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort("not a list")

def test_quick_sort_incomparable_elements():
    """Test handling of incomparable elements."""
    with pytest.raises(TypeError, match="List contains elements that cannot be compared"):
        quick_sort([1, 2, "3", 4])

def test_quick_sort_with_mixed_types():
    """Test sorting of lists with numeric types."""
    arr = [3, 1.5, 2, -4, 0]
    assert quick_sort(arr) == [-4, 0, 1.5, 2, 3]