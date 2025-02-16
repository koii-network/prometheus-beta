import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_basic_sorted_arrays():
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6]

def test_merge_unequal_length_arrays():
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 7, 9]

def test_merge_empty_arrays():
    arr1 = []
    arr2 = []
    result = merge_sorted_arrays(arr1, arr2)
    assert result == []

def test_merge_one_empty_array():
    arr1 = [1, 2, 3]
    arr2 = []
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3]

def test_merge_with_duplicates():
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 2, 2, 3, 3, 4]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        merge_sorted_arrays("not a list", [1, 2, 3])

def test_unsorted_input_arrays():
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [1, 2, 3])