import pytest
from src.common_element_checker import has_common_element

def test_has_common_element_true():
    # Test case with common element
    arr1 = [1, 2, 3, 4]
    arr2 = [4, 5, 6, 7]
    assert has_common_element(arr1, arr2) == True

def test_has_common_element_false():
    # Test case with no common element
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert has_common_element(arr1, arr2) == False

def test_has_common_element_empty_arrays():
    # Test case with empty arrays
    arr1 = []
    arr2 = []
    assert has_common_element(arr1, arr2) == False

def test_has_common_element_one_empty_array():
    # Test case with one empty array
    arr1 = [1, 2, 3]
    arr2 = []
    assert has_common_element(arr1, arr2) == False

def test_has_common_element_same_arrays():
    # Test case with identical arrays
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]
    assert has_common_element(arr1, arr2) == True

def test_has_common_element_different_types():
    # Test case with different data types
    arr1 = [1, 'a', 3.14]
    arr2 = ['b', 3.14, 4]
    assert has_common_element(arr1, arr2) == True