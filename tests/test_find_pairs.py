import pytest
from src.find_pairs import find_pairs_sum_to_target

def test_find_pairs_sum_to_target_basic():
    # Test basic scenario
    numbers = [1, 2, 3, 4, 5]
    target = 7
    result = find_pairs_sum_to_target(numbers, target)
    assert sorted(result) == sorted([(2, 5), (3, 4)])

def test_find_pairs_sum_to_target_no_pairs():
    # Test when no pairs sum to target
    numbers = [1, 2, 3, 4, 5]
    target = 100
    result = find_pairs_sum_to_target(numbers, target)
    assert result == []

def test_find_pairs_sum_to_target_duplicate_numbers():
    # Test with duplicate numbers
    numbers = [3, 3, 3, 4, 5]
    target = 6
    result = find_pairs_sum_to_target(numbers, target)
    assert sorted(result) == sorted([(3, 3)])

def test_find_pairs_sum_to_target_empty_list():
    # Test with an empty list
    numbers = []
    target = 10
    result = find_pairs_sum_to_target(numbers, target)
    assert result == []

def test_find_pairs_sum_to_target_negative_numbers():
    # Test with negative numbers
    numbers = [-1, -2, 3, 4, 5]
    target = 2
    result = find_pairs_sum_to_target(numbers, target)
    assert sorted(result) == sorted([(-1, 3)])