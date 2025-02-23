import pytest
from src.count_pairs_diff_5 import count_pairs_with_difference_5

def test_basic_pairs():
    """Test basic scenarios with pairs having a difference of 5"""
    assert count_pairs_with_difference_5([1, 6, 3, 8, 2, 7]) == 2
    assert count_pairs_with_difference_5([6, 1, 11, 6, 11]) == 2

def test_no_pairs():
    """Test scenarios with no pairs having a difference of 5"""
    assert count_pairs_with_difference_5([1, 2, 3, 4, 5]) == 0
    assert count_pairs_with_difference_5([10, 20, 30, 40]) == 0

def test_edge_cases():
    """Test edge cases"""
    assert count_pairs_with_difference_5([]) == 0
    assert count_pairs_with_difference_5([5]) == 0
    assert count_pairs_with_difference_5([5, 10]) == 1
    assert count_pairs_with_difference_5([10, 5]) == 1

def test_multiple_pairs():
    """Test scenarios with multiple pairs"""
    assert count_pairs_with_difference_5([1, 6, 6, 1, 11, 16]) == 3