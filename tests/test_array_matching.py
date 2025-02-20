import pytest
from src.array_matching import count_matching_elements

def test_count_matching_elements_basic():
    # Basic case with some matching elements
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert count_matching_elements(arr1, arr2) == 3

def test_count_matching_elements_no_matches():
    # Case with no matching elements
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert count_matching_elements(arr1, arr2) == 0

def test_count_matching_elements_all_matches():
    # Case where all elements match
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3, 4, 5]
    assert count_matching_elements(arr1, arr2) == 3

def test_count_matching_elements_empty_arrays():
    # Case with empty arrays
    arr1 = []
    arr2 = [1, 2, 3]
    assert count_matching_elements(arr1, arr2) == 0

def test_count_matching_elements_with_duplicates():
    # Case with duplicate elements
    arr1 = [1, 1, 2, 2, 3, 3]
    arr2 = [2, 3, 4, 5]
    assert count_matching_elements(arr1, arr2) == 4