import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_basic_increasing_sequence():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert longest_increasing_subsequence(arr) == 5

def test_monotonically_increasing_sequence():
    arr = [1, 2, 3, 4, 5]
    assert longest_increasing_subsequence(arr) == 5

def test_monotonically_decreasing_sequence():
    arr = [5, 4, 3, 2, 1]
    assert longest_increasing_subsequence(arr) == 1

def test_empty_array():
    arr = []
    assert longest_increasing_subsequence(arr) == 0

def test_single_element_array():
    arr = [42]
    assert longest_increasing_subsequence(arr) == 1

def test_array_with_duplicates():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert longest_increasing_subsequence(arr) == 6

def test_all_same_elements():
    arr = [7, 7, 7, 7, 7]
    assert longest_increasing_subsequence(arr) == 1