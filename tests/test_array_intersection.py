import pytest
from src.array_intersection import find_array_intersection

def test_find_array_intersection_basic():
    """Test basic intersection of two arrays"""
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    assert sorted(find_array_intersection(arr1, arr2)) == [4, 5]

def test_find_array_intersection_no_common_elements():
    """Test when there are no common elements"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert find_array_intersection(arr1, arr2) == []

def test_find_array_intersection_duplicate_elements():
    """Test with duplicate elements in input arrays"""
    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 2, 4, 5, 6]
    assert sorted(find_array_intersection(arr1, arr2)) == [2, 4]

def test_find_array_intersection_empty_arrays():
    """Test with empty input arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert find_array_intersection(arr1, arr2) == []

def test_find_array_intersection_identical_arrays():
    """Test when both arrays are identical"""
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]
    assert sorted(find_array_intersection(arr1, arr2)) == [1, 2, 3]