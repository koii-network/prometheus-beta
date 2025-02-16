import pytest
from src.cycle_sort import cycle_sort

def test_cycle_sort_basic():
    """Test basic sorting of a random list"""
    arr = [5, 2, 9, 1, 7, 6, 3]
    sorted_arr = cycle_sort(arr)  # in-place sorting
    assert sorted_arr == sorted(arr)
    assert arr == sorted(arr)  # Ensure in-place sorting

def test_cycle_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    sorted_arr = cycle_sort(arr)
    assert sorted_arr == []

def test_cycle_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    sorted_arr = cycle_sort(arr)
    assert sorted_arr == [42]

def test_cycle_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    sorted_arr = cycle_sort(arr)
    assert sorted_arr == arr

def test_cycle_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    sorted_arr = cycle_sort(arr)
    assert sorted_arr == sorted(arr)

def test_cycle_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    sorted_arr = cycle_sort(arr)
    assert sorted_arr == sorted(arr)

def test_cycle_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 2, -1, 0, 9, -3]
    sorted_arr = cycle_sort(arr)
    assert sorted_arr == sorted(arr)

def test_cycle_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        cycle_sort("not a list")
    with pytest.raises(TypeError):
        cycle_sort(123)