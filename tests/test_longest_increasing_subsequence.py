import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_case():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert find_longest_increasing_subsequence(arr) == [10, 22, 33, 50, 60]

def test_empty_array():
    assert find_longest_increasing_subsequence([]) == []

def test_single_element():
    assert find_longest_increasing_subsequence([5]) == [5]

def test_descending_array():
    arr = [5, 4, 3, 2, 1]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_all_equal_elements():
    arr = [2, 2, 2, 2, 2]
    assert find_longest_increasing_subsequence(arr) == [2]

def test_multiple_valid_subsequences():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    # There could be multiple valid longest increasing subsequences
    result = find_longest_increasing_subsequence(arr)
    assert len(result) == 6  # Longest subsequence length is 6
    assert result == [0, 2, 6, 9, 13, 15]

def test_negative_numbers():
    arr = [-1, -2, 0, 3, 5, -3, 1, 2]
    assert find_longest_increasing_subsequence(arr) == [-2, 0, 1, 2]