import pytest
from src.array_intersection import find_array_intersection

def test_basic_intersection():
    """Test basic intersection of two arrays"""
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    assert find_array_intersection(arr1, arr2) == [4, 5]

def test_no_intersection():
    """Test when there are no common elements"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert find_array_intersection(arr1, arr2) == []

def test_full_intersection():
    """Test when all elements are common"""
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]
    assert find_array_intersection(arr1, arr2) == [1, 2, 3]

def test_duplicate_elements():
    """Test arrays with duplicate elements"""
    arr1 = [1, 2, 2, 3, 4, 4]
    arr2 = [2, 2, 4, 5, 6]
    assert find_array_intersection(arr1, arr2) == [2, 4]

def test_empty_arrays():
    """Test intersection with empty arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert find_array_intersection(arr1, arr2) == []
    assert find_array_intersection(arr2, arr1) == []

def test_large_numbers():
    """Test intersection with large numbers"""
    arr1 = [1000000, 2000000, 3000000]
    arr2 = [2000000, 3000000, 4000000]
    assert find_array_intersection(arr1, arr2) == [2000000, 3000000]