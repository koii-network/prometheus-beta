import pytest
from src.two_sum_check import two_sum_check

def test_two_sum_check_basic_true():
    """Test case where two numbers sum to target"""
    assert two_sum_check([1, 2, 3, 4], 7) == True

def test_two_sum_check_basic_false():
    """Test case where no two numbers sum to target"""
    assert two_sum_check([1, 2, 3, 4], 10) == False

def test_two_sum_check_empty_array():
    """Test with an empty array"""
    assert two_sum_check([], 5) == False

def test_two_sum_check_single_element():
    """Test with single element array"""
    assert two_sum_check([5], 10) == False

def test_two_sum_check_negative_numbers():
    """Test with negative numbers"""
    assert two_sum_check([-1, -2, -3, 3, 4], 1) == True

def test_two_sum_check_zero_sum():
    """Test with zero sum"""
    assert two_sum_check([0, 0], 0) == True

def test_two_sum_check_large_array():
    """Test with larger array"""
    large_array = list(range(1000))
    assert two_sum_check(large_array, 1998) == True
    assert two_sum_check(large_array, 2000) == False