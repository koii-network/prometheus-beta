import pytest
from src.pair_sum_finder import find_pairs_sum_to_target

def test_basic_pair_finding():
    """Test finding pairs that sum to a target"""
    assert find_pairs_sum_to_target([1, 2, 3, 4, 5], 7) == [(2, 5), (3, 4)]

def test_single_solution():
    """Test finding a single pair"""
    assert find_pairs_sum_to_target([1, 1, 2, 3, 4], 5) == [(1, 4), (2, 3)]

def test_no_solution():
    """Test when no pairs sum to target"""
    assert find_pairs_sum_to_target([1, 2, 3, 4], 10) == []

def test_empty_list():
    """Test with an empty list"""
    assert find_pairs_sum_to_target([], 5) == []

def test_single_element_list():
    """Test with a list containing only one element"""
    assert find_pairs_sum_to_target([5], 10) == []

def test_multiple_same_pair():
    """Test with multiple occurrences of the same pair"""
    result = find_pairs_sum_to_target([1, 4, 4, 2, 3, 5], 5)
    assert result == [(1, 4), (2, 3)]

def test_negative_numbers():
    """Test with negative numbers"""
    assert find_pairs_sum_to_target([-1, 0, 1, 2, -2, 3], 1) == [(-2, 3), (-1, 2), (0, 1)]

def test_zero_target():
    """Test with zero as the target"""
    assert find_pairs_sum_to_target([-1, 0, 1, 2, -2], 0) == [(-2, 2), (-1, 1)]

def test_repeated_unique_pairs():
    """Test handling of repeated but unique pairs"""
    result = find_pairs_sum_to_target([1, 2, 2, 3, 3, 4], 5)
    assert result == [(1, 4), (2, 3)]