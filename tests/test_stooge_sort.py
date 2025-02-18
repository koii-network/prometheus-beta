import pytest
from src.stooge_sort import stooge_sort

def test_stooge_sort_empty_list():
    """Test sorting an empty list."""
    assert stooge_sort([]) == []

def test_stooge_sort_single_element():
    """Test sorting a list with a single element."""
    assert stooge_sort([5]) == [5]

def test_stooge_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    assert stooge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_stooge_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    assert stooge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_stooge_sort_random_list():
    """Test sorting a random unsorted list."""
    assert stooge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_stooge_sort_with_duplicates():
    """Test sorting a list with duplicate values."""
    assert stooge_sort([3, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 9]

def test_stooge_sort_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        stooge_sort("not a list")
    with pytest.raises(TypeError):
        stooge_sort(123)
    with pytest.raises(TypeError):
        stooge_sort(None)