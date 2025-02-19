import pytest
from src.longest_subsequence import longest_subsequence_with_sum

def test_basic_subsequence():
    # Basic scenario with positive numbers
    assert longest_subsequence_with_sum([1, 2, 3, 4, 5], 9) == 3

def test_empty_array():
    # Empty array should return 0
    assert longest_subsequence_with_sum([], 5) == 0

def test_negative_numbers():
    # Array with negative numbers
    assert longest_subsequence_with_sum([1, -1, 5, -2, 3], 3) == 4

def test_all_zeros():
    # Array with all zeros
    assert longest_subsequence_with_sum([0, 0, 0, 0], 0) == 4

def test_no_subsequence():
    # No subsequence matches the target
    assert longest_subsequence_with_sum([1, 2, 3], 10) == 0

def test_multiple_subsequences():
    # Multiple possible subsequences
    assert longest_subsequence_with_sum([3, 1, 2, 4, 3], 6) == 3

def test_single_element_match():
    # Single element matches target
    assert longest_subsequence_with_sum([5, 1, 2, 3], 5) == 1

def test_mixed_numbers():
    # Mixed positive and negative numbers
    assert longest_subsequence_with_sum([10, 5, -5, 3, -2, 7, -1], 8) == 4