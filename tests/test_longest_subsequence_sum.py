import pytest
from src.longest_subsequence_sum import longest_subsequence_with_target_sum

def test_basic_scenarios():
    # Basic test cases
    assert longest_subsequence_with_target_sum([1, 2, 3, 4, 5], 9) == 2  # [2, 3, 4]
    assert longest_subsequence_with_target_sum([1, 1, 1, 1], 2) == 2  # Multiple possible subsequences
    assert longest_subsequence_with_target_sum([3, 1, 2, 4, 3], 6) == 2  # [3, 3]

def test_edge_cases():
    # Edge case tests
    assert longest_subsequence_with_target_sum([], 5) == 0  # Empty array
    assert longest_subsequence_with_target_sum([1, 2, 3], 10) == 0  # No subsequence matches
    assert longest_subsequence_with_target_sum([1, 2, 3], 6) == 3  # Entire array is the subsequence

def test_negative_numbers():
    # Test with negative numbers
    assert longest_subsequence_with_target_sum([-1, 1, 2, -2, 3, -3], 0) == 3  # Subsequence with zero sum
    assert longest_subsequence_with_target_sum([-2, -1, 2, 3, 4], 1) == 2  # Mixed positive and negative

def test_repeated_numbers():
    # Test with repeated numbers
    assert longest_subsequence_with_target_sum([2, 2, 2, 2, 2], 4) == 2  # Multiple ways to get the sum
    assert longest_subsequence_with_target_sum([1, 2, 1, 2, 1], 3) == 2  # Non-contiguous subsequence