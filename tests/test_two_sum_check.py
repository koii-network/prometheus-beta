import pytest
from src.two_sum_check import two_sum_check

def test_two_sum_check_basic_positive():
    """Test a basic case where two numbers sum to the target"""
    assert two_sum_check([1, 2, 3, 4, 5], 7) == True

def test_two_sum_check_basic_negative():
    """Test a case where no two numbers sum to the target"""
    assert two_sum_check([1, 2, 3, 4, 5], 20) == False

def test_two_sum_check_empty_list():
    """Test with an empty list"""
    assert two_sum_check([], 5) == False

def test_two_sum_check_single_element():
    """Test with a single element list"""
    assert two_sum_check([5], 10) == False

def test_two_sum_check_duplicate_values():
    """Test with duplicate values that sum to target"""
    assert two_sum_check([3, 3], 6) == True

def test_two_sum_check_negative_numbers():
    """Test with negative numbers"""
    assert two_sum_check([-1, -2, 3, 4], 2) == True

def test_two_sum_check_zero_sum():
    """Test with zero as target sum"""
    assert two_sum_check([-1, 1, 2, 3], 0) == True