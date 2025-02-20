import pytest
from src.two_sum import two_sum

def test_two_sum_basic():
    """Test basic functionality of two_sum"""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_no_solution():
    """Test when no solution exists"""
    assert two_sum([1, 2, 3, 4], 10) == []

def test_two_sum_multiple_solutions():
    """Test when multiple solutions exist"""
    result = two_sum([3, 2, 4], 6)
    assert result == [1, 2]

def test_two_sum_same_number():
    """Test when the same number can't be used twice"""
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum_empty_list():
    """Test with an empty list"""
    assert two_sum([], 5) == []

def test_two_sum_negative_numbers():
    """Test with negative numbers"""
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]