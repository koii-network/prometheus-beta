import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_sorted_arrays_basic():
    # Test merging two sorted arrays
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_arrays_different_lengths():
    # Test merging arrays of different lengths
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 7, 9]

def test_merge_sorted_arrays_empty():
    # Test merging with an empty array
    arr1 = [1, 2, 3]
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]

def test_merge_sorted_arrays_both_empty():
    # Test merging two empty arrays
    arr1 = []
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == []

def test_merge_sorted_arrays_with_duplicates():
    # Test merging arrays with duplicate elements
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4, 5]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 2, 2, 3, 3, 4, 5]