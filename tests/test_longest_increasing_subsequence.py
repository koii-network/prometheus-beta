import pytest
from src.longest_increasing_subsequence import longest_continuous_increasing_subsequence

def test_basic_increasing_sequence():
    assert longest_continuous_increasing_subsequence([1,3,5,4,7]) == 3

def test_all_same_elements():
    assert longest_continuous_increasing_subsequence([2,2,2,2,2]) == 1

def test_empty_array():
    assert longest_continuous_increasing_subsequence([]) == 0

def test_full_increasing_sequence():
    assert longest_continuous_increasing_subsequence([1,2,3,4,5]) == 5

def test_single_element():
    assert longest_continuous_increasing_subsequence([42]) == 1

def test_decreasing_sequence():
    assert longest_continuous_increasing_subsequence([5,4,3,2,1]) == 1

def test_mixed_sequence():
    assert longest_continuous_increasing_subsequence([1,3,5,7,2,4,6,8]) == 4