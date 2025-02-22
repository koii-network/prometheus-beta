import pytest
from src.introsort import introsort

def test_empty_list():
    assert introsort([]) == []

def test_single_element():
    assert introsort([5]) == [5]

def test_sorted_list():
    arr = [1, 2, 3, 4, 5]
    assert introsort(arr) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    arr = [5, 4, 3, 2, 1]
    assert introsort(arr) == [1, 2, 3, 4, 5]

def test_random_list():
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert introsort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_duplicate_elements():
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert introsort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_large_list():
    arr = list(range(1000, 0, -1))
    assert introsort(arr) == list(range(1, 1001))

def test_floating_point_numbers():
    arr = [3.14, 2.71, 1.41, 0.58]
    assert introsort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_negative_numbers():
    arr = [-5, -2, -10, -1, -8]
    assert introsort(arr) == [-10, -8, -5, -2, -1]

def test_mixed_numbers():
    arr = [-3, 4, 0, 2, -1, 5]
    assert introsort(arr) == [-3, -1, 0, 2, 4, 5]