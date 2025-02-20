import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_empty_list():
    assert longest_increasing_subsequence([]) == 0
    assert longest_increasing_subsequence([], return_subsequence=True) == []

def test_single_element():
    assert longest_increasing_subsequence([5]) == 1
    assert longest_increasing_subsequence([5], return_subsequence=True) == [5]

def test_increasing_sequence():
    arr = [10, 22, 33, 44, 55]
    assert longest_increasing_subsequence(arr) == 5
    assert longest_increasing_subsequence(arr, return_subsequence=True) == [10, 22, 33, 44, 55]

def test_non_consecutive_lis():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert longest_increasing_subsequence(arr) == 5
    assert longest_increasing_subsequence(arr, return_subsequence=True) == [10, 22, 33, 50, 60]

def test_repeated_elements():
    arr = [7, 7, 7, 7, 7, 7]
    assert longest_increasing_subsequence(arr) == 1
    assert longest_increasing_subsequence(arr, return_subsequence=True) == [7]

def test_unsorted_input():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert longest_increasing_subsequence(arr) == 4
    assert longest_increasing_subsequence(arr, return_subsequence=True) == [1, 4, 5, 9]

def test_invalid_input():
    with pytest.raises(TypeError):
        longest_increasing_subsequence("not a list")
    
    with pytest.raises(ValueError):
        longest_increasing_subsequence([1, 2, 'a', 3])