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

def test_merge_sorted_arrays_empty_first():
    """Test merging when first array is empty"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]

def test_merge_sorted_arrays_empty_second():
    """Test merging when second array is empty"""
    arr1 = [1, 2, 3]
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]

def test_merge_sorted_arrays_both_empty():
    """Test merging when both arrays are empty"""
    arr1 = []
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == []

def test_merge_sorted_arrays_with_duplicates():
    """Test merging arrays with duplicate values"""
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4, 5]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 2, 2, 3, 3, 4, 5]