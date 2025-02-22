import pytest
from src.find_occurrences import find_first_last_occurrence

def test_find_occurrences_multiple_occurrences():
    arr = [1, 2, 2, 2, 3, 4, 4, 5]
    assert find_first_last_occurrence(arr, 2) == (1, 3)
    assert find_first_last_occurrence(arr, 4) == (5, 6)

def test_find_occurrences_single_occurrence():
    arr = [1, 3, 5, 7, 9]
    assert find_first_last_occurrence(arr, 5) == (2, 2)

def test_find_occurrences_not_found():
    arr = [1, 3, 5, 7, 9]
    assert find_first_last_occurrence(arr, 4) == (-1, -1)
    assert find_first_last_occurrence(arr, 0) == (-1, -1)
    assert find_first_last_occurrence(arr, 10) == (-1, -1)

def test_find_occurrences_edge_cases():
    # Empty array
    assert find_first_last_occurrence([], 5) == (-1, -1)
    
    # Array with single element
    arr_single = [5]
    assert find_first_last_occurrence(arr_single, 5) == (0, 0)
    assert find_first_last_occurrence(arr_single, 6) == (-1, -1)

def test_find_occurrences_first_and_last_element():
    arr = [1, 1, 2, 3, 4, 4, 4, 5, 5, 5]
    assert find_first_last_occurrence(arr, 1) == (0, 1)
    assert find_first_last_occurrence(arr, 5) == (7, 9)