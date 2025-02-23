import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_basic_sorted_arrays():
    """Test merging two basic sorted arrays"""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_with_empty_arrays():
    """Test merging with empty arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]
    assert merge_sorted_arrays(arr2, arr1) == [1, 2, 3]
    assert merge_sorted_arrays([], []) == []

def test_merge_duplicate_elements():
    """Test merging arrays with duplicate elements"""
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 4, 5]
    expected = [1, 2, 2, 2, 3, 4, 5]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_different_length_arrays():
    """Test merging arrays of different lengths"""
    arr1 = [1, 5, 7]
    arr2 = [2, 3, 4, 6, 8, 9]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        merge_sorted_arrays("not a list", [1, 2, 3])
    with pytest.raises(TypeError):
        merge_sorted_arrays([1, 2, 3], "not a list")
    with pytest.raises(TypeError):
        merge_sorted_arrays(None, [1, 2, 3])

def test_unsorted_input_arrays():
    """Test handling of unsorted input arrays"""
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        merge_sorted_arrays([1, 2, 3], [3, 1, 2])

def test_single_element_arrays():
    """Test merging single-element arrays"""
    arr1 = [1]
    arr2 = [2]
    expected = [1, 2]
    assert merge_sorted_arrays(arr1, arr2) == expected