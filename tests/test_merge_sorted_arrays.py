import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_basic_sorted_arrays():
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_different_length_arrays():
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 7, 9]

def test_merge_empty_arrays():
    arr1 = []
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == []

def test_merge_one_empty_array():
    arr1 = [1, 2, 3]
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]
    assert merge_sorted_arrays(arr2, arr1) == [1, 2, 3]

def test_merge_with_duplicates():
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 2, 2, 3, 3, 4]

def test_merge_negative_numbers():
    arr1 = [-3, -1, 0]
    arr2 = [-2, 1, 2]
    assert merge_sorted_arrays(arr1, arr2) == [-3, -2, -1, 0, 1, 2]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        merge_sorted_arrays("not a list", [1, 2, 3])
    with pytest.raises(TypeError):
        merge_sorted_arrays([1, 2, 3], "not a list")

def test_unsorted_input():
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        merge_sorted_arrays([1, 2, 3], [3, 1, 2])