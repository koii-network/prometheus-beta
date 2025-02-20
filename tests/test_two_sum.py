import pytest
from src.two_sum import find_two_sum

def test_find_two_sum_basic():
    """Test basic functionality of find_two_sum"""
    assert find_two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_find_two_sum_no_solution():
    """Test when no solution exists"""
    assert find_two_sum([1, 2, 3, 4], 10) == []

def test_find_two_sum_multiple_solutions():
    """Test when multiple solutions could exist, return the first found"""
    assert find_two_sum([3, 2, 4], 6) == [1, 2]

def test_find_two_sum_negative_numbers():
    """Test with negative numbers"""
    assert find_two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_find_two_sum_empty_array():
    """Test with an empty array"""
    assert find_two_sum([], 5) == []

def test_find_two_sum_same_number():
    """Test when the same number is used twice"""
    assert find_two_sum([3, 3], 6) == [0, 1]

def test_find_two_sum_large_array():
    """Test with a larger array"""
    large_array = list(range(1, 1001))
    assert find_two_sum(large_array, 1999) == [998, 999]