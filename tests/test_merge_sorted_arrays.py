import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_basic_sorted_arrays():
    """Test merging two basic sorted arrays"""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_with_duplicates():
    """Test merging arrays with duplicate elements"""
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4, 5]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 2, 2, 3, 3, 4, 5]

def test_merge_one_empty_array():
    """Test merging with one empty array"""
    arr1 = [1, 2, 3]
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]
    assert merge_sorted_arrays([], arr1) == [1, 2, 3]

def test_merge_both_empty_arrays():
    """Test merging two empty arrays"""
    assert merge_sorted_arrays([], []) == []

def test_merge_different_length_arrays():
    """Test merging arrays of different lengths"""
    arr1 = [1, 5, 7]
    arr2 = [2, 3, 4, 6, 8, 9]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_unsorted_input_raises_error():
    """Test that unsorted input raises a ValueError"""
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [4, 5, 6])
    with pytest.raises(ValueError):
        merge_sorted_arrays([1, 2, 3], [6, 5, 4])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError):
        merge_sorted_arrays("not a list", [1, 2, 3])
    with pytest.raises(TypeError):
        merge_sorted_arrays([1, 2, 3], "not a list")
    with pytest.raises(TypeError):
        merge_sorted_arrays(None, [1, 2, 3])