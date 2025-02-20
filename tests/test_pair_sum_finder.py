import pytest
from src.pair_sum_finder import find_pairs_with_target_sum

def test_find_pairs_with_target_sum_basic():
    # Basic case with multiple pairs
    arr = [1, 2, 3, 4, 5, 6]
    target = 7
    expected = [(1, 6), (2, 5), (3, 4)]
    assert sorted(find_pairs_with_target_sum(arr, target)) == sorted(expected)

def test_find_pairs_with_target_sum_no_pairs():
    # Case with no pairs found
    arr = [1, 2, 3, 4, 5]
    target = 10
    assert find_pairs_with_target_sum(arr, target) == []

def test_find_pairs_with_target_sum_single_pair():
    # Case with only one pair
    arr = [1, 2, 3, 4, 5, 6]
    target = 11
    expected = [(5, 6)]
    assert find_pairs_with_target_sum(arr, target) == expected

def test_find_pairs_with_target_sum_empty_array():
    # Case with empty array
    arr = []
    target = 5
    assert find_pairs_with_target_sum(arr, target) == []

def test_find_pairs_with_target_sum_invalid_input():
    # Test invalid input types
    with pytest.raises(ValueError, match="Input must be a list"):
        find_pairs_with_target_sum(123, 10)
    
    with pytest.raises(ValueError, match="Input array must contain unique elements"):
        find_pairs_with_target_sum([1, 2, 2, 3], 4)

def test_find_pairs_with_target_sum_edge_cases():
    # Various edge cases
    arr = [-1, 0, 1, 2, 3, 4]
    target = 0
    expected = [(-1, 1)]
    assert find_pairs_with_target_sum(arr, target) == expected