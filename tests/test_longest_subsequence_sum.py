import pytest
from src.longest_subsequence_sum import longest_subsequence_with_target_sum

def test_basic_positive_cases():
    # Basic test cases
    assert longest_subsequence_with_target_sum([1, 2, 3, 4, 5], 9) == 3  # [2, 3, 4]
    assert longest_subsequence_with_target_sum([1, 1, 1, 1, 1], 3) == 3  # [1, 1, 1]

def test_edge_cases():
    # Empty array
    assert longest_subsequence_with_target_sum([], 5) == 0
    
    # No subsequence matching target
    assert longest_subsequence_with_target_sum([1, 2, 3], 10) == 0

def test_complex_cases():
    # Mixed positive and negative numbers
    assert longest_subsequence_with_target_sum([10, 5, -5, 3, 2, 7], 8) == 3  # [5, -5, 8]
    
    # All negative numbers
    assert longest_subsequence_with_target_sum([-1, -2, -3, -4], -6) == 2

def test_multiple_valid_subsequences():
    # Multiple possible subsequences, return longest
    assert longest_subsequence_with_target_sum([1, 2, 1, 2, 1], 3) == 2

def test_large_numbers():
    # Test with larger numbers
    assert longest_subsequence_with_target_sum([100, 200, 300, 400], 500) == 2  # [100, 400]