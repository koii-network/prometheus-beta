import pytest
from src.common_element_checker import has_common_element

def test_has_common_element_true():
    """Test that the function returns True when arrays have a common element"""
    arr1 = [1, 2, 3, 4]
    arr2 = [4, 5, 6]
    assert has_common_element(arr1, arr2) == True

def test_has_common_element_false():
    """Test that the function returns False when arrays have no common elements"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert has_common_element(arr1, arr2) == False

def test_has_common_element_empty_arrays():
    """Test function with empty arrays"""
    arr1 = []
    arr2 = []
    assert has_common_element(arr1, arr2) == False

def test_has_common_element_one_empty_array():
    """Test function when one array is empty"""
    arr1 = [1, 2, 3]
    arr2 = []
    assert has_common_element(arr1, arr2) == False

def test_has_common_element_string_arrays():
    """Test function with string arrays"""
    arr1 = ['apple', 'banana', 'cherry']
    arr2 = ['date', 'cherry', 'elderberry']
    assert has_common_element(arr1, arr2) == True

def test_has_common_element_duplicate_common_element():
    """Test function with duplicate common element"""
    arr1 = [1, 1, 2, 3]
    arr2 = [4, 1, 5]
    assert has_common_element(arr1, arr2) == True