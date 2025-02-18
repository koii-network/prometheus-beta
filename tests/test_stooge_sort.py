import pytest
from src.stooge_sort import stooge_sort

def test_stooge_sort_basic():
    """Test basic sorting functionality."""
    assert stooge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_stooge_sort_already_sorted():
    """Test sorting an already sorted list."""
    assert stooge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_stooge_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    assert stooge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_stooge_sort_empty_list():
    """Test sorting an empty list."""
    assert stooge_sort([]) == []

def test_stooge_sort_single_element():
    """Test sorting a list with a single element."""
    assert stooge_sort([42]) == [42]

def test_stooge_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    assert stooge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_stooge_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    assert stooge_sort([-3, -1, -4, 0, 5, -9, 2]) == [-9, -4, -3, -1, 0, 2, 5]

def test_stooge_sort_type_error():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        stooge_sort("not a list")
    with pytest.raises(TypeError):
        stooge_sort(123)