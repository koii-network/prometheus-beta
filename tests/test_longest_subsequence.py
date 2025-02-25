import pytest
from src.longest_subsequence import longest_subsequence_with_target_sum

def test_basic_positive_sequence():
    """Test a basic scenario with a positive subsequence"""
    arr = [1, 2, 3, 4, 5]
    target = 9
    assert longest_subsequence_with_target_sum(arr, target) == 3

def test_empty_array():
    """Test an empty array returns 0"""
    arr = []
    target = 5
    assert longest_subsequence_with_target_sum(arr, target) == 0

def test_no_matching_subsequence():
    """Test when no subsequence matches the target"""
    arr = [1, 2, 3, 4, 5]
    target = 100
    assert longest_subsequence_with_target_sum(arr, target) == 0

def test_entire_array_matches():
    """Test when the entire array matches the target"""
    arr = [1, 2, 3, 4]
    target = 10
    assert longest_subsequence_with_target_sum(arr, target) == 4

def test_multiple_subsequences():
    """Test when multiple subsequences exist"""
    arr = [1, 1, 1, 2, 3, 4, 1, 1, 1]
    target = 5
    # Expect the first valid longest subsequence
    assert longest_subsequence_with_target_sum(arr, target) == 4

def test_negative_numbers():
    """Test with negative numbers in the array"""
    arr = [-1, 2, -3, 4, 5, -2, 3]
    target = 5
    # Expect the first valid subsequence
    assert longest_subsequence_with_target_sum(arr, target) == 6

def test_zero_target():
    """Test with zero as the target"""
    arr = [0, 0, 1, -1, 2]
    target = 0
    # Expect the first valid subsequence
    assert longest_subsequence_with_target_sum(arr, target) == 4

def test_large_numbers():
    """Test with large numbers"""
    arr = [10000, 20000, 30000, 40000]
    target = 50000
    assert longest_subsequence_with_target_sum(arr, target) == 2