import pytest
from src.max_increasing_subsequence_sum import max_increasing_subsequence_sum

def test_basic_increasing_sequence():
    assert max_increasing_subsequence_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_sequence():
    assert max_increasing_subsequence_sum([10, 9, 2, 5, 3, 7, 101, 18]) == 38

def test_empty_sequence():
    assert max_increasing_subsequence_sum([]) == 0

def test_single_element():
    assert max_increasing_subsequence_sum([42]) == 42

def test_duplicate_elements():
    assert max_increasing_subsequence_sum([1, 1, 1, 1]) == 1

def test_negative_numbers():
    assert max_increasing_subsequence_sum([-2, -1, 0, 1]) == 0

def test_large_sequence():
    large_seq = list(range(1, 1001))
    assert max_increasing_subsequence_sum(large_seq) == sum(range(1, 1001))

def test_random_complex_sequence():
    assert max_increasing_subsequence_sum([3, 1, 4, 1, 5, 9, 2, 6, 5]) == 14