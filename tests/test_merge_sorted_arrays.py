import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_sorted_arrays_basic():
    """Test merging two sorted arrays of equal length"""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_arrays_unequal_length():
    """Test merging sorted arrays of different lengths"""
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 7, 9]

def test_merge_sorted_arrays_one_empty():
    """Test merging with one empty array"""
    arr1 = [1, 2, 3]
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]

def test_merge_sorted_arrays_both_empty():
    """Test merging two empty arrays"""
    arr1 = []
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == []

def test_merge_sorted_arrays_type_error():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        merge_sorted_arrays("not a list", [1, 2, 3])
    with pytest.raises(TypeError):
        merge_sorted_arrays([1, 2, 3], "not a list")

def test_merge_sorted_arrays_value_error():
    """Test that ValueError is raised for unsorted input arrays"""
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [4, 5, 6])
    with pytest.raises(ValueError):
        merge_sorted_arrays([1, 2, 3], [6, 5, 4])