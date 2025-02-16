import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_sorted_arrays_normal_case():
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_one_empty():
    arr1 = [1, 2, 3]
    arr2 = []
    expected = [1, 2, 3]
    assert merge_sorted_arrays(arr1, arr2) == expected
    assert merge_sorted_arrays(arr2, arr1) == expected

def test_merge_sorted_arrays_both_empty():
    arr1 = []
    arr2 = []
    expected = []
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_with_duplicates():
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4, 5]
    expected = [1, 2, 2, 2, 3, 3, 4, 5]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_different_lengths():
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4]
    expected = [1, 2, 3, 4, 5, 7]
    assert merge_sorted_arrays(arr1, arr2) == expected