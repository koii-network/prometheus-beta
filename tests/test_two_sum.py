import pytest
from src.two_sum import two_sum

def test_two_sum_basic():
    """Test basic scenario with a valid solution"""
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]

def test_two_sum_multiple_solutions():
    """Test when multiple solutions exist"""
    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2]

def test_two_sum_no_solution():
    """Test when no solution exists"""
    nums = [1, 2, 3, 4]
    target = 10
    assert two_sum(nums, target) == []

def test_two_sum_same_elements():
    """Test with multiple same elements"""
    nums = [3, 3]
    target = 6
    assert two_sum(nums, target) == [0, 1]

def test_two_sum_empty_array():
    """Test with an empty array"""
    nums = []
    target = 5
    assert two_sum(nums, target) == []

def test_two_sum_negative_numbers():
    """Test with negative numbers"""
    nums = [-1, -2, -3, -4, -5]
    target = -8
    assert two_sum(nums, target) == [2, 4]