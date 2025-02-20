import pytest
from src.bubble_sort import optimized_bubble_sort

def test_normal_sorting():
    """Test sorting a list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert optimized_bubble_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_already_sorted_list():
    """Test that an already sorted list is returned unchanged."""
    arr = [1, 2, 3, 4, 5]
    assert optimized_bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert optimized_bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test handling of an empty list."""
    arr = []
    assert optimized_bubble_sort(arr) == []

def test_single_element_list():
    """Test handling of a single-element list."""
    arr = [42]
    assert optimized_bubble_sort(arr) == [42]

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert optimized_bubble_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        optimized_bubble_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        optimized_bubble_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        optimized_bubble_sort(None)