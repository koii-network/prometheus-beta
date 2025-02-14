import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_sorted_arrays_basic():
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_unequal_lengths():
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4]
    expected = [1, 2, 3, 4, 5, 7, 9]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_empty_lists():
    arr1 = []
    arr2 = []
    expected = []
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_one_empty_list():
    arr1 = [1, 2, 3]
    arr2 = []
    expected = [1, 2, 3]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_with_duplicates():
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 4, 4]
    expected = [1, 2, 2, 2, 3, 4, 4]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_invalid_type():
    with pytest.raises(TypeError):
        merge_sorted_arrays("not a list", [1, 2, 3])

def test_merge_sorted_arrays_unsorted():
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [1, 2, 3])