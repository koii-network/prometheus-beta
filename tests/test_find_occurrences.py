import pytest
from src.find_occurrences import find_first_last_occurrence

def test_multiple_occurrences():
    arr = [1, 2, 2, 2, 3, 4, 4, 5]
    assert find_first_last_occurrence(arr, 2) == (1, 3)
    assert find_first_last_occurrence(arr, 4) == (5, 6)

def test_single_occurrence():
    arr = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 3) == (2, 2)

def test_element_not_found():
    arr = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 6) == (-1, -1)
    assert find_first_last_occurrence(arr, 0) == (-1, -1)

def test_empty_array():
    arr = []
    assert find_first_last_occurrence(arr, 1) == (-1, -1)

def test_first_last_element():
    arr = [1, 1, 2, 3, 4, 5, 5]
    assert find_first_last_occurrence(arr, 1) == (0, 1)
    assert find_first_last_occurrence(arr, 5) == (5, 6)

def test_all_same_elements():
    arr = [2, 2, 2, 2, 2]
    assert find_first_last_occurrence(arr, 2) == (0, 4)