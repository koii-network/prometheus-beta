import pytest
from src.two_sum import two_sum

def test_two_sum_basic():
    """Test basic functionality of two_sum"""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum_no_solution():
    """Test case where no solution exists"""
    assert two_sum([1, 2, 3, 4], 10) == []
    assert two_sum([], 5) == []

def test_two_sum_large_array():
    """Test with a larger array"""
    nums = list(range(1000))
    target = 1998
    result = two_sum(nums, target)
    assert len(result) == 2
    assert nums[result[0]] + nums[result[1]] == target

def test_two_sum_negative_numbers():
    """Test with negative numbers"""
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_two_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]