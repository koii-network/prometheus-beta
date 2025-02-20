import pytest
from src.binary_search import binary_search

def test_binary_search_normal_case():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binary_search(arr, 5) == 4

def test_binary_search_first_occurrence():
    arr = [1, 2, 2, 2, 3, 4, 5]
    assert binary_search(arr, 2) == 1

def test_binary_search_target_not_found():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 6) == -1

def test_binary_search_empty_array():
    arr = []
    assert binary_search(arr, 5) == -1

def test_binary_search_single_element_found():
    arr = [5]
    assert binary_search(arr, 5) == 0

def test_binary_search_single_element_not_found():
    arr = [5]
    assert binary_search(arr, 6) == -1

def test_binary_search_multiple_occurrences():
    arr = [1, 2, 2, 2, 3, 4, 5]
    assert binary_search(arr, 2) == 1