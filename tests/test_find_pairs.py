import pytest
from src.find_pairs import find_pairs_sum_to_target

def test_find_pairs_basic():
    """Test basic functionality of finding pairs"""
    numbers = [1, 2, 3, 4, 5]
    target = 7
    expected = [(2, 5), (3, 4)]
    assert sorted(find_pairs_sum_to_target(numbers, target)) == sorted(expected)

def test_find_pairs_empty_list():
    """Test with an empty list"""
    numbers = []
    target = 10
    assert find_pairs_sum_to_target(numbers, target) == []

def test_find_pairs_no_matches():
    """Test when no pairs sum to target"""
    numbers = [1, 2, 3, 4, 5]
    target = 100
    assert find_pairs_sum_to_target(numbers, target) == []

def test_find_pairs_duplicate_numbers():
    """Test with duplicate numbers in the list"""
    numbers = [1, 3, 3, 4, 5, 5]
    target = 6
    expected = [(1, 5), (3, 3)]
    assert sorted(find_pairs_sum_to_target(numbers, target)) == sorted(expected)

def test_find_pairs_negative_numbers():
    """Test with negative numbers"""
    numbers = [-1, -2, 3, 4, 5, 6]
    target = 4
    expected = [(-2, 6), (3, 1)]
    assert sorted(find_pairs_sum_to_target(numbers, target)) == sorted(expected)

def test_find_pairs_zero_target():
    """Test with zero as the target"""
    numbers = [-2, 0, 2, 4, -4]
    target = 0
    expected = [(-2, 2), (-4, 4)]
    assert sorted(find_pairs_sum_to_target(numbers, target)) == sorted(expected)

def test_find_pairs_large_list():
    """Test with a larger list of numbers"""
    numbers = list(range(1, 100))
    target = 50
    expected = [(1, 49), (2, 48), (3, 47), (4, 46), (5, 45), 
                (6, 44), (7, 43), (8, 42), (9, 41), (10, 40), 
                (11, 39), (12, 38), (13, 37), (14, 36), (15, 35), 
                (16, 34), (17, 33), (18, 32), (19, 31), (20, 30), 
                (21, 29), (22, 28), (23, 27), (24, 26), (25, 25)]
    assert sorted(find_pairs_sum_to_target(numbers, target)) == sorted(expected)