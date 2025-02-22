import pytest
from src.array_intersection import find_array_intersection

def test_basic_intersection():
    """Test basic intersection of two arrays"""
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    assert set(find_array_intersection(arr1, arr2)) == {4, 5}

def test_no_intersection():
    """Test arrays with no common elements"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert find_array_intersection(arr1, arr2) == []

def test_duplicate_elements():
    """Test arrays with duplicate elements"""
    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 2, 4, 5, 6]
    assert set(find_array_intersection(arr1, arr2)) == {2, 4}

def test_empty_arrays():
    """Test intersection with empty arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert find_array_intersection(arr1, arr2) == []

def test_same_array():
    """Test intersection of an array with itself"""
    arr1 = [1, 2, 3, 4]
    assert set(find_array_intersection(arr1, arr1)) == {1, 2, 3, 4}

def test_large_arrays():
    """Test intersection of large arrays"""
    arr1 = list(range(1000))
    arr2 = list(range(500, 1500))
    expected = set(range(500, 1000))
    assert set(find_array_intersection(arr1, arr2)) == expected