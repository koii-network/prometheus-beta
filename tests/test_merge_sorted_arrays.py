import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_sorted_arrays_basic():
    """Test merging two sorted arrays with multiple elements"""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6], "Should merge arrays in sorted order"

def test_merge_sorted_arrays_different_lengths():
    """Test merging sorted arrays of different lengths"""
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 7, 9], "Should handle arrays of different lengths"

def test_merge_sorted_arrays_one_empty():
    """Test merging when one array is empty"""
    arr1 = [1, 2, 3]
    arr2 = []
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3], "Should return the non-empty array when one is empty"

def test_merge_sorted_arrays_both_empty():
    """Test merging when both arrays are empty"""
    arr1 = []
    arr2 = []
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [], "Should return an empty array when both input arrays are empty"

def test_merge_sorted_arrays_with_duplicates():
    """Test merging arrays with duplicate elements"""
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 2, 2, 3, 3, 4], "Should handle arrays with duplicate elements"