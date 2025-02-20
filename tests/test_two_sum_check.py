import pytest
from src.two_sum_check import two_sum_check

def test_two_sum_check_positive_case():
    """Test case where two numbers sum up to the target"""
    nums = [1, 2, 3, 4, 5]
    target_sum = 7
    assert two_sum_check(nums, target_sum) == True

def test_two_sum_check_negative_case():
    """Test case where no two numbers sum up to the target"""
    nums = [1, 2, 3, 4, 5]
    target_sum = 100
    assert two_sum_check(nums, target_sum) == False

def test_two_sum_check_empty_array():
    """Test case with an empty array"""
    nums = []
    target_sum = 10
    assert two_sum_check(nums, target_sum) == False

def test_two_sum_check_single_element():
    """Test case with a single element array"""
    nums = [5]
    target_sum = 10
    assert two_sum_check(nums, target_sum) == False

def test_two_sum_check_negative_numbers():
    """Test case with negative numbers"""
    nums = [-1, -2, 3, 4, 5]
    target_sum = 2
    assert two_sum_check(nums, target_sum) == True

def test_two_sum_check_zero_target():
    """Test case with zero as target sum"""
    nums = [-1, 1, 2, 3, 4]
    target_sum = 0
    assert two_sum_check(nums, target_sum) == True