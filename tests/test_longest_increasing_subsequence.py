import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_empty_array():
    assert longest_increasing_subsequence([]) == 0

def test_single_element():
    assert longest_increasing_subsequence([5]) == 1

def test_all_increasing():
    assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5

def test_unsorted_increasing_subsequence():
    assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]) == 5

def test_descending_array():
    assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1

def test_mixed_sequence():
    assert longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_duplicate_elements():
    assert longest_increasing_subsequence([1, 2, 2, 3, 3, 4, 4, 5]) == 5

def test_negative_numbers():
    assert longest_increasing_subsequence([-1, -2, 0, 1, 2, -1, 3]) == 5