import pytest
from src.longest_consecutive_sequence import find_longest_consecutive_sequence

def test_longest_consecutive_sequence_basic():
    assert find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == [1, 2, 3, 4]

def test_longest_consecutive_sequence_empty_list():
    assert find_longest_consecutive_sequence([]) == []

def test_longest_consecutive_sequence_no_consecutive():
    assert find_longest_consecutive_sequence([5, 10, 15, 20]) == [5]

def test_longest_consecutive_sequence_multiple_same_length():
    result = find_longest_consecutive_sequence([1, 2, 3, 10, 11, 12])
    assert result in [[1, 2, 3], [10, 11, 12]]

def test_longest_consecutive_sequence_repeated_numbers():
    assert find_longest_consecutive_sequence([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]

def test_longest_consecutive_sequence_negative_numbers():
    assert find_longest_consecutive_sequence([-7, -6, -5, -4, 1, 3, 4]) == [-7, -6, -5, -4]