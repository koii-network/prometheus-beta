import pytest
from src.cycle_sort import cycle_sort

def test_cycle_sort_normal_list():
    """Test sorting a normal list of integers"""
    arr = [5, 2, 9, 1, 7, 6, 3]
    expected = [1, 2, 3, 5, 6, 7, 9]
    assert cycle_sort(arr) == expected

def test_cycle_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert cycle_sort(arr) == arr

def test_cycle_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert cycle_sort(arr) == expected

def test_cycle_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    expected = [1, 2, 2, 3, 3, 4, 8]
    assert cycle_sort(arr) == expected

def test_cycle_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert cycle_sort(arr) == arr

def test_cycle_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert cycle_sort(arr) == []

def test_cycle_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        cycle_sort("not a list")
    with pytest.raises(TypeError):
        cycle_sort(123)
    with pytest.raises(TypeError):
        cycle_sort(None)