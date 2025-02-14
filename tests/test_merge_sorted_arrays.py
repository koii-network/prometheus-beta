import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_sorted_arrays_basic():
    # Test basic scenario with two sorted arrays
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_arrays_different_lengths():
    # Test arrays of different lengths
    arr1 = [1, 4, 7, 8, 10]
    arr2 = [2, 3, 5]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 7, 8, 10]

def test_merge_sorted_arrays_empty_array():
    # Test merging with an empty array
    arr1 = [1, 2, 3]
    arr2 = []
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3]

def test_merge_sorted_arrays_both_empty():
    # Test merging two empty arrays
    arr1 = []
    arr2 = []
    result = merge_sorted_arrays(arr1, arr2)
    assert result == []

def test_merge_sorted_arrays_with_duplicates():
    # Test merging arrays with duplicate values
    arr1 = [1, 2, 2, 4]
    arr2 = [1, 3, 4, 5]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 1, 2, 2, 3, 4, 4, 5]