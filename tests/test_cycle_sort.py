import pytest
from src.cycle_sort import cycle_sort

def test_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert cycle_sort(arr) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    arr = [42]
    assert cycle_sort(arr) == [42]

def test_already_sorted_list():
    """Test a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert cycle_sort(arr) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test a list sorted in descending order."""
    arr = [5, 4, 3, 2, 1]
    assert cycle_sort(arr) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test a list with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert cycle_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_negative_numbers():
    """Test a list with negative numbers."""
    arr = [-5, 3, 0, -2, 7, 1]
    assert cycle_sort(arr) == [-5, -2, 0, 1, 3, 7]

def test_mixed_numbers():
    """Test a list with mixed positive and negative numbers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert cycle_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        cycle_sort("not a list")
    with pytest.raises(TypeError):
        cycle_sort(123)
    with pytest.raises(TypeError):
        cycle_sort(None)