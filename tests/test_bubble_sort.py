import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_normal_list():
    """Test sorting a normal list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_bubble_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_bubble_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert bubble_sort(arr) == []

def test_bubble_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert bubble_sort(arr) == [42]

def test_bubble_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bubble_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bubble_sort_with_strings():
    """Test sorting a list of strings."""
    arr = ['banana', 'apple', 'cherry', 'date']
    assert bubble_sort(arr) == ['apple', 'banana', 'cherry', 'date']

def test_bubble_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bubble_sort("not a list")

def test_bubble_sort_incomparable_types():
    """Test that a TypeError is raised for incomparable types."""
    with pytest.raises(TypeError, match="List contains elements that cannot be compared"):
        bubble_sort([1, 'a', 2])