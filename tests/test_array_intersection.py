import pytest
from src.array_intersection import find_array_intersection

def test_find_array_intersection_basic():
    """Test basic intersection of two arrays"""
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    assert find_array_intersection(arr1, arr2) == [4, 5]

def test_find_array_intersection_no_common():
    """Test arrays with no common elements"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert find_array_intersection(arr1, arr2) == []

def test_find_array_intersection_duplicate_elements():
    """Test arrays with duplicate elements"""
    arr1 = [1, 2, 2, 3, 3, 4]
    arr2 = [2, 2, 3, 4, 4, 5]
    assert find_array_intersection(arr1, arr2) == [2, 3, 4]

def test_find_array_intersection_empty_arrays():
    """Test with empty arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert find_array_intersection(arr1, arr2) == []
    assert find_array_intersection(arr2, arr1) == []

def test_find_array_intersection_large_inputs():
    """Test with larger input arrays"""
    arr1 = list(range(1000))
    arr2 = list(range(500, 1500))
    expected = list(range(500, 1000))
    assert find_array_intersection(arr1, arr2) == expected