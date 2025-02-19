import pytest
from src.find_pairs_sum_to_target import find_pairs_sum_to_target

def test_find_pairs_sum_to_target_basic():
    """Test basic functionality of finding pairs"""
    numbers = [1, 2, 3, 4, 5]
    target = 7
    expected = [[2, 5], [3, 4]]
    result = find_pairs_sum_to_target(numbers, target)
    assert sorted(result) == sorted(expected)

def test_find_pairs_sum_to_target_no_pairs():
    """Test when no pairs sum to the target"""
    numbers = [1, 2, 3, 4, 5]
    target = 100
    expected = []
    result = find_pairs_sum_to_target(numbers, target)
    assert result == expected

def test_find_pairs_sum_to_target_duplicate_numbers():
    """Test with duplicate numbers in the list"""
    numbers = [1, 3, 3, 4, 5, 5]
    target = 8
    expected = [[3, 5]]
    result = find_pairs_sum_to_target(numbers, target)
    assert sorted(result) == sorted(expected)

def test_find_pairs_sum_to_target_unique_pairs():
    """Test that pairs are unique"""
    numbers = [1, 2, 2, 3, 4, 4, 5]
    target = 6
    expected = [[1, 5], [2, 4]]
    result = find_pairs_sum_to_target(numbers, target)
    assert sorted(result) == sorted(expected)

def test_find_pairs_sum_to_target_empty_list():
    """Test with an empty list"""
    numbers = []
    target = 10
    expected = []
    result = find_pairs_sum_to_target(numbers, target)
    assert result == expected