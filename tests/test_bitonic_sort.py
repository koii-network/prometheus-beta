import pytest
from src.bitonic_sort import bitonic_sort

def test_bitonic_sort_ascending():
    """Test bitonic sort in ascending order"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bitonic_sort(arr)
    assert sorted_arr == sorted(arr)
    assert sorted_arr is not arr  # Ensure original list is not modified

def test_bitonic_sort_descending():
    """Test bitonic sort in descending order"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bitonic_sort(arr, ascending=False)
    assert sorted_arr == sorted(arr, reverse=True)

def test_bitonic_sort_empty_list():
    """Test bitonic sort with an empty list"""
    arr = []
    sorted_arr = bitonic_sort(arr)
    assert sorted_arr == []

def test_bitonic_sort_single_element():
    """Test bitonic sort with a single-element list"""
    arr = [42]
    sorted_arr = bitonic_sort(arr)
    assert sorted_arr == [42]

def test_bitonic_sort_already_sorted():
    """Test bitonic sort with an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    sorted_arr = bitonic_sort(arr)
    assert sorted_arr == arr

def test_bitonic_sort_reverse_sorted():
    """Test bitonic sort with a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    sorted_arr = bitonic_sort(arr)
    assert sorted_arr == sorted(arr)

def test_bitonic_sort_duplicate_elements():
    """Test bitonic sort with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = bitonic_sort(arr)
    assert sorted_arr == sorted(arr)

def test_bitonic_sort_invalid_input():
    """Test bitonic sort with invalid input"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")
    with pytest.raises(TypeError):
        bitonic_sort(None)