import pytest
from src.binary_search import binary_search

def test_binary_search_typical_cases():
    # Test typical scenario with sorted array
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 1) == 0
    assert binary_search([1, 3, 5, 7, 9], 9) == 4

def test_binary_search_not_found():
    # Test cases where target is not in the array
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search([1, 3, 5, 7, 9], 0) == -1
    assert binary_search([1, 3, 5, 7, 9], 10) == -1

def test_binary_search_empty_array():
    # Test empty array scenario
    assert binary_search([], 5) == -1

def test_binary_search_single_element_array():
    # Test array with single element
    assert binary_search([5], 5) == 0
    assert binary_search([5], 6) == -1

def test_binary_search_large_array():
    # Test with a larger sorted array
    large_array = list(range(1000))
    assert binary_search(large_array, 500) == 500
    assert binary_search(large_array, 999) == 999
    assert binary_search(large_array, 1000) == -1