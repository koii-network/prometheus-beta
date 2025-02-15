import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_basic():
    """Test merging two sorted arrays"""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_unequal_lengths():
    """Test merging arrays of different lengths"""
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 7, 9]

def test_merge_with_duplicates():
    """Test merging arrays with duplicate values"""
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4, 5]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 2, 2, 3, 3, 4, 5]

def test_one_empty_array():
    """Test merging with an empty array"""
    arr1 = [1, 2, 3]
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]

def test_both_empty_arrays():
    """Test merging two empty arrays"""
    arr1 = []
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == []

def test_invalid_input_types():
    """Test handling of non-list inputs"""
    with pytest.raises(TypeError, match="Inputs must be lists"):
        merge_sorted_arrays("not a list", [1, 2, 3])

def test_unsorted_arrays():
    """Test handling of unsorted input arrays"""
    with pytest.raises(ValueError, match="Input arrays must be sorted"):
        merge_sorted_arrays([3, 1, 2], [1, 2, 3])