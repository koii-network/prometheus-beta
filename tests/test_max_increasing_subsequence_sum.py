import pytest
from src.max_increasing_subsequence_sum import max_increasing_subsequence_sum

def test_empty_array():
    assert max_increasing_subsequence_sum([]) == 0

def test_single_element():
    assert max_increasing_subsequence_sum([5]) == 5

def test_all_increasing():
    assert max_increasing_subsequence_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_sequence():
    assert max_increasing_subsequence_sum([10, 22, 9, 33, 21, 50, 41, 60]) == 155

def test_negative_numbers():
    assert max_increasing_subsequence_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_random_sequence():
    assert max_increasing_subsequence_sum([2, 100, 3, 4, 5, 1, 6]) == 116

def test_descending_sequence():
    assert max_increasing_subsequence_sum([5, 4, 3, 2, 1]) == 5