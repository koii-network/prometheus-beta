import pytest
from src.cycle_sort import cycle_sort

def test_cycle_sort_normal_list():
    """Test cycle sort with a normal unsorted list"""
    arr = [5, 2, 9, 1, 7, 6, 3]
    result = cycle_sort(arr)
    assert result == [1, 2, 3, 5, 6, 7, 9]
    assert arr == [1, 2, 3, 5, 6, 7, 9]  # Ensure in-place sorting

def test_cycle_sort_already_sorted():
    """Test cycle sort with an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    result = cycle_sort(arr)
    assert result == [1, 2, 3, 4, 5]

def test_cycle_sort_reverse_sorted():
    """Test cycle sort with a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    result = cycle_sort(arr)
    assert result == [1, 2, 3, 4, 5]

def test_cycle_sort_with_duplicates():
    """Test cycle sort with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    result = cycle_sort(arr)
    assert result == [1, 2, 2, 3, 3, 4, 8]

def test_cycle_sort_empty_list():
    """Test cycle sort with an empty list"""
    arr = []
    result = cycle_sort(arr)
    assert result == []

def test_cycle_sort_single_element():
    """Test cycle sort with a single element"""
    arr = [42]
    result = cycle_sort(arr)
    assert result == [42]

def test_cycle_sort_invalid_input():
    """Test cycle sort with invalid input type"""
    with pytest.raises(TypeError):
        cycle_sort("not a list")
    with pytest.raises(TypeError):
        cycle_sort(123)
    with pytest.raises(TypeError):
        cycle_sort(None)