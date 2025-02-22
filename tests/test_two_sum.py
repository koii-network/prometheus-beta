import pytest
from src.two_sum import two_sum

def test_two_sum_positive_case():
    """Test that the function returns True when a pair summing to target exists"""
    assert two_sum([1, 2, 3, 4], 7) == True
    assert two_sum([10, 15, 3, 7], 17) == True

def test_two_sum_negative_case():
    """Test that the function returns False when no pair summing to target exists"""
    assert two_sum([1, 2, 3, 4], 10) == False
    assert two_sum([5, 6, 7, 8], 3) == False

def test_two_sum_edge_cases():
    """Test edge cases including empty list and single element list"""
    assert two_sum([], 5) == False
    assert two_sum([5], 10) == False

def test_two_sum_zero_target():
    """Test cases with zero as the target"""
    assert two_sum([-1, 1, 2, 3], 0) == True
    assert two_sum([1, 2, 3], 0) == False

def test_two_sum_negative_numbers():
    """Test with negative numbers"""
    assert two_sum([-1, -2, -3, -4], -7) == True
    assert two_sum([-1, -2, -3, -4], 0) == False