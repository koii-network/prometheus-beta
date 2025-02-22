import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_standard_case():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 5
    assert subsequence == [10, 22, 33, 50, 60]

def test_empty_array():
    arr = []
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 0
    assert subsequence == []

def test_single_element():
    arr = [42]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 1
    assert subsequence == [42]

def test_all_descending():
    arr = [5, 4, 3, 2, 1]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 1
    assert subsequence == [5] or subsequence == [4] or subsequence == [3] or \
           subsequence == [2] or subsequence == [1]

def test_already_sorted():
    arr = [1, 2, 3, 4, 5]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 5
    assert subsequence == [1, 2, 3, 4, 5]

def test_multiple_possible_subsequences():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 6
    # One of the possible valid subsequences
    assert subsequence == [0, 2, 6, 9, 13, 15]