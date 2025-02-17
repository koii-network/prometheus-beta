import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_basic_sorted_arrays():
    """Test merging two basic sorted arrays"""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6]

def test_merge_with_duplicates():
    """Test merging sorted arrays with duplicate values"""
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4, 5]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 2, 2, 3, 3, 4, 5]

def test_merge_different_lengths():
    """Test merging arrays of different lengths"""
    arr1 = [1, 5, 7]
    arr2 = [2, 3, 4, 6, 8, 9]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_merge_one_empty_array():
    """Test merging when one array is empty"""
    arr1 = [1, 2, 3]
    arr2 = []
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3]

def test_merge_both_empty_arrays():
    """Test merging when both arrays are empty"""
    arr1 = []
    arr2 = []
    result = merge_sorted_arrays(arr1, arr2)
    assert result == []

def test_invalid_input_type():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        merge_sorted_arrays(1, [2, 3])
    with pytest.raises(TypeError):
        merge_sorted_arrays([1, 2], "not a list")

def test_unsorted_input():
    """Test that ValueError is raised for unsorted inputs"""
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        merge_sorted_arrays([1, 2, 3], [3, 1, 2])