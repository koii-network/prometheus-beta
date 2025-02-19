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

def test_multiple_duplicates():
    """Test arrays with multiple duplicate common elements"""
    arr1 = [1, 2, 2, 3, 3, 4]
    arr2 = [2, 2, 3, 3, 5, 6]
    assert set(find_array_intersection(arr1, arr2)) == {2, 3}

def test_empty_arrays():
    """Test intersection with empty arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert find_array_intersection(arr1, arr2) == []

def test_identical_arrays():
    """Test intersection of identical arrays"""
    arr1 = [1, 2, 3, 4]
    arr2 = [1, 2, 3, 4]
    assert set(find_array_intersection(arr1, arr2)) == {1, 2, 3, 4}