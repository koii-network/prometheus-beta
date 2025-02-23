import pytest
from src.cycle_sort import cycle_sort

def test_cycle_sort_basic():
    """Test basic sorting functionality"""
    arr = [5, 2, 9, 1, 7, 6, 3]
    assert cycle_sort(arr) == [1, 2, 3, 5, 6, 7, 9]

def test_cycle_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert cycle_sort(arr) == [1, 2, 3, 4, 5]

def test_cycle_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert cycle_sort(arr) == [1, 2, 3, 4, 5]

def test_cycle_sort_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert cycle_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_cycle_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert cycle_sort(arr) == []

def test_cycle_sort_single_element():
    """Test sorting a single-element list"""
    arr = [42]
    assert cycle_sort(arr) == [42]

def test_cycle_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 2, -10, 0, 7]
    assert cycle_sort(arr) == [-10, -5, 0, 2, 7]

def test_cycle_sort_invalid_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        cycle_sort("not a list")

def test_cycle_sort_in_place():
    """Test that the original list is modified in-place"""
    arr = [5, 2, 9, 1, 7]
    original_id = id(arr)
    cycle_sort(arr)
    assert id(arr) == original_id
    assert arr == [1, 2, 5, 7, 9]