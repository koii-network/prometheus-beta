import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_basic_increasing_sequence():
    arr = [10, 22, 33, 44, 55]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 5
    assert subsequence == arr

def test_mixed_sequence():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 5
    assert subsequence == [10, 22, 33, 50, 60]

def test_empty_list():
    arr = []
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 0
    assert subsequence == []

def test_single_element():
    arr = [42]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 1
    assert subsequence == [42]

def test_repeated_sequence():
    arr = [7, 7, 7, 7, 7, 7]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 1
    assert subsequence == [7]

def test_non_consecutive_increasing_sequence():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 6
    assert subsequence == [0, 2, 6, 9, 13, 15]