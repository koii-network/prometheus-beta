import pytest
from src.insertion_sort import insertion_sort

def test_insertion_sort_normal_list():
    """Test sorting a normal list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert insertion_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_insertion_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]

def test_insertion_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]

def test_insertion_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert insertion_sort(arr) == []

def test_insertion_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert insertion_sort(arr) == [42]

def test_insertion_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert insertion_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_insertion_sort_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort(123)