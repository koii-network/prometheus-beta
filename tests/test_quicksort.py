import pytest
from src.quicksort import quicksort

def test_quicksort_empty_list():
    """Test sorting an empty list."""
    assert quicksort([]) == []

def test_quicksort_single_element():
    """Test sorting a list with a single element."""
    assert quicksort([5]) == [5]

def test_quicksort_already_sorted():
    """Test sorting an already sorted list."""
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted():
    """Test sorting a reverse sorted list."""
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_quicksort_unsorted_list():
    """Test sorting an unsorted list."""
    assert quicksort([3, 6, 1, 8, 2, 4]) == [1, 2, 3, 4, 6, 8]

def test_quicksort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_quicksort_negative_numbers():
    """Test sorting a list with negative numbers."""
    assert quicksort([-3, -1, -4, 0, 2, -2]) == [-4, -3, -2, -1, 0, 2]

def test_quicksort_type_error():
    """Test that a TypeError is raised when input is not a list."""
    with pytest.raises(TypeError):
        quicksort("not a list")
        quicksort(123)
        quicksort(None)