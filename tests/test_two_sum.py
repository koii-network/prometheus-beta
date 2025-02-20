import pytest
from src.two_sum import find_two_sum

def test_find_two_sum_basic():
    """Test basic functionality of finding two sum pairs"""
    numbers = [1, 2, 3, 4, 5]
    target_sum = 7
    expected = [(2, 5), (3, 4)]
    assert sorted(find_two_sum(numbers, target_sum)) == sorted(expected)

def test_find_two_sum_no_pairs():
    """Test scenario where no pairs sum to target"""
    numbers = [1, 2, 3, 4, 5]
    target_sum = 20
    assert find_two_sum(numbers, target_sum) == []

def test_find_two_sum_multiple_pairs():
    """Test finding multiple unique pairs"""
    numbers = [1, 2, 3, 4, 5, 6, 7]
    target_sum = 8
    expected = [(1, 7), (2, 6), (3, 5)]
    assert sorted(find_two_sum(numbers, target_sum)) == sorted(expected)

def test_find_two_sum_empty_list():
    """Test with an empty list"""
    numbers = []
    target_sum = 10
    assert find_two_sum(numbers, target_sum) == []

def test_find_two_sum_single_element():
    """Test with a single element list"""
    numbers = [5]
    target_sum = 10
    assert find_two_sum(numbers, target_sum) == []

def test_find_two_sum_negative_numbers():
    """Test with negative numbers"""
    numbers = [-1, -2, -3, 0, 1, 2, 3]
    target_sum = 0
    expected = [(-3, 3), (-2, 2), (-1, 1)]
    assert sorted(find_two_sum(numbers, target_sum)) == sorted(expected)