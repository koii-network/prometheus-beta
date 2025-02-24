import pytest
from src.merge_sorted_arrays import merge_sorted_arrays, is_sorted

def test_merge_basic_sorted_arrays():
    """Test merging two basic sorted arrays"""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_unequal_length_arrays():
    """Test merging sorted arrays of different lengths"""
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 7, 9]

def test_merge_with_duplicate_elements():
    """Test merging sorted arrays with duplicate elements"""
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4, 5]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 2, 2, 3, 3, 4, 5]

def test_merge_empty_arrays():
    """Test merging empty arrays"""
    arr1 = []
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == []

def test_merge_one_empty_array():
    """Test merging when one array is empty"""
    arr1 = [1, 2, 3]
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]
    assert merge_sorted_arrays(arr2, arr1) == [1, 2, 3]

def test_is_sorted_function():
    """Test the helper is_sorted function"""
    assert is_sorted([]) == True
    assert is_sorted([1]) == True
    assert is_sorted([1, 2, 3]) == True
    assert is_sorted([1, 1, 2]) == True
    assert is_sorted([3, 2, 1]) == False

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        merge_sorted_arrays("not a list", [1, 2, 3])
    with pytest.raises(TypeError):
        merge_sorted_arrays([1, 2, 3], "not a list")

def test_unsorted_input_arrays():
    """Test error handling for unsorted input arrays"""
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        merge_sorted_arrays([1, 2, 3], [3, 1, 2])