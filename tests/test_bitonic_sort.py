import pytest
from src.bitonic_sort import bitonic_sort

def test_bitonic_sort_ascending():
    """Test bitonic sort in ascending order"""
    arr = [3, 7, 4, 8, 6, 2, 1, 5]
    expected = sorted(arr)
    assert bitonic_sort(arr) == expected

def test_bitonic_sort_descending():
    """Test bitonic sort in descending order"""
    arr = [3, 7, 4, 8, 6, 2, 1, 5]
    expected = sorted(arr, reverse=True)
    assert bitonic_sort(arr, ascending=False) == expected

def test_bitonic_sort_empty_list():
    """Test bitonic sort with an empty list"""
    assert bitonic_sort([]) == []

def test_bitonic_sort_single_element():
    """Test bitonic sort with a single-element list"""
    arr = [42]
    assert bitonic_sort(arr) == arr

def test_bitonic_sort_already_sorted():
    """Test bitonic sort with an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert bitonic_sort(arr) == arr

def test_bitonic_sort_reverse_sorted():
    """Test bitonic sort with a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    expected = sorted(arr)
    assert bitonic_sort(arr) == expected

def test_bitonic_sort_invalid_input():
    """Test bitonic sort with invalid input"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")

def test_bitonic_sort_with_duplicates():
    """Test bitonic sort with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(arr)
    assert bitonic_sort(arr) == expected