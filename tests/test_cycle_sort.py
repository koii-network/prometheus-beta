import pytest
from src.cycle_sort import cycle_sort

def test_cycle_sort_normal_list():
    """Test cycle sort with a normal list of integers."""
    arr = [5, 2, 9, 1, 7, 6, 3]
    assert cycle_sort(arr) == [1, 2, 3, 5, 6, 7, 9]

def test_cycle_sort_already_sorted():
    """Test cycle sort with an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert cycle_sort(arr) == [1, 2, 3, 4, 5]

def test_cycle_sort_reverse_sorted():
    """Test cycle sort with a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert cycle_sort(arr) == [1, 2, 3, 4, 5]

def test_cycle_sort_with_duplicates():
    """Test cycle sort with a list containing duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert cycle_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_cycle_sort_empty_list():
    """Test cycle sort with an empty list."""
    arr = []
    assert cycle_sort(arr) == []

def test_cycle_sort_single_element():
    """Test cycle sort with a single-element list."""
    arr = [42]
    assert cycle_sort(arr) == [42]

def test_cycle_sort_negative_numbers():
    """Test cycle sort with negative numbers."""
    arr = [-5, 2, -10, 0, 7, 3]
    assert cycle_sort(arr) == [-10, -5, 0, 2, 3, 7]

def test_cycle_sort_invalid_input():
    """Test cycle sort with invalid input type."""
    with pytest.raises(TypeError):
        cycle_sort("not a list")
    with pytest.raises(TypeError):
        cycle_sort(123)