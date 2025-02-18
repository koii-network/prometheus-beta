import pytest
from src.cycle_sort import cycle_sort

def test_cycle_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert cycle_sort(arr) == []

def test_cycle_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [5]
    assert cycle_sort(arr) == [5]

def test_cycle_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert cycle_sort(arr) == [1, 2, 3, 4, 5]

def test_cycle_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    assert cycle_sort(arr) == [1, 2, 3, 4, 5]

def test_cycle_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert cycle_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_cycle_sort_random_order():
    """Test sorting a list in random order."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert cycle_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_cycle_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-5, 12, 0, -3, 8]
    assert cycle_sort(arr) == [-5, -3, 0, 8, 12]

def test_cycle_sort_invalid_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        cycle_sort("not a list")
    with pytest.raises(TypeError):
        cycle_sort(123)
    with pytest.raises(TypeError):
        cycle_sort(None)