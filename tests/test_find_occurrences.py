import pytest
from src.find_occurrences import find_first_last_occurrence

def test_find_occurrences_normal_case():
    arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
    assert find_first_last_occurrence(arr, 2) == (1, 3)
    assert find_first_last_occurrence(arr, 5) == (6, 8)

def test_find_occurrences_single_element():
    arr = [3]
    assert find_first_last_occurrence(arr, 3) == (0, 0)

def test_find_occurrences_element_not_found():
    arr = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 6) == (-1, -1)

def test_find_occurrences_empty_array():
    arr = []
    assert find_first_last_occurrence(arr, 1) == (-1, -1)

def test_find_occurrences_multiple_identical_elements():
    arr = [1, 1, 1, 1, 1]
    assert find_first_last_occurrence(arr, 1) == (0, 4)

def test_find_occurrences_large_sorted_array():
    arr = list(range(1000)) + list(range(1000, 2000)) * 2 + list(range(2000, 3000))
    assert find_first_last_occurrence(arr, 1500) == (1500, 3499)