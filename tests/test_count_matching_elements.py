import pytest
from src.count_matching_elements import count_matching_elements

def test_basic_matching():
    """Test basic case with some matching elements"""
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    assert count_matching_elements(arr1, arr2) == 2

def test_no_matching_elements():
    """Test case with no matching elements"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert count_matching_elements(arr1, arr2) == 0

def test_all_matching_elements():
    """Test case where all elements match"""
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3, 4, 5]
    assert count_matching_elements(arr1, arr2) == 3

def test_empty_arrays():
    """Test case with empty arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert count_matching_elements(arr1, arr2) == 0

def test_duplicate_elements():
    """Test case with duplicate elements in arr1"""
    arr1 = [1, 1, 2, 2, 3, 3]
    arr2 = [1, 2, 4]
    assert count_matching_elements(arr1, arr2) == 4

def test_different_types_same_value():
    """Test case with different types that are considered equal"""
    arr1 = [1, '1', 2, 3]
    arr2 = [1, 4, 5]
    assert count_matching_elements(arr1, arr2) == 1