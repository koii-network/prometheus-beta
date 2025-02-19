import pytest
from src.zero_sum_pairs import count_zero_sum_pairs

def test_basic_zero_sum_pairs():
    # Test basic scenario with multiple zero-sum pairs
    assert count_zero_sum_pairs([1, -1, 2, -2, 3]) == 2

def test_empty_array():
    # Test empty array returns 0
    assert count_zero_sum_pairs([]) == 0

def test_multiple_zero_pairs():
    # Test multiple instances of the same pair
    assert count_zero_sum_pairs([0, 0, 0]) == 3

def test_no_zero_sum_pairs():
    # Test array with no zero-sum pairs
    assert count_zero_sum_pairs([1, 2, 3, 4, 5]) == 0

def test_negative_and_positive_pairs():
    # Test mix of negative and positive numbers
    assert count_zero_sum_pairs([-1, 1, -2, 2, 3, -3]) == 3

def test_large_numbers():
    # Test with large numbers
    assert count_zero_sum_pairs([1000000, -1000000, 500000, -500000]) == 2

def test_duplicate_numbers():
    # Test with duplicate numbers
    assert count_zero_sum_pairs([1, 1, -1, -1]) == 2