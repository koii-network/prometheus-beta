import pytest
from src.count_matching_elements import count_matching_elements

def test_basic_matching():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert count_matching_elements(arr1, arr2) == 3

def test_no_matching_elements():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert count_matching_elements(arr1, arr2) == 0

def test_all_matching_elements():
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3, 4, 5]
    assert count_matching_elements(arr1, arr2) == 3

def test_empty_arrays():
    arr1 = []
    arr2 = [1, 2, 3]
    assert count_matching_elements(arr1, arr2) == 0

def test_duplicate_elements():
    arr1 = [1, 1, 2, 2, 3]
    arr2 = [2, 3, 4]
    assert count_matching_elements(arr1, arr2) == 3

def test_type_preservation():
    arr1 = [1, 2, 3, 'a']
    arr2 = [3, 'a', 4, 5]
    assert count_matching_elements(arr1, arr2) == 2