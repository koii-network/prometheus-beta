import pytest
from src.calculate_sum import calculate_sum

def test_calculate_sum_normal_case():
    """Test with a standard list of integers"""
    test_list = [1, 2, 3, 4, 5]
    assert calculate_sum(test_list) == (1*0 + 2*1 + 3*2 + 4*3 + 5*4)

def test_calculate_sum_empty_list():
    """Test with an empty list"""
    assert calculate_sum([]) == 0

def test_calculate_sum_negative_numbers():
    """Test with list containing negative numbers"""
    test_list = [-1, -2, -3, -4, -5]
    assert calculate_sum(test_list) == (-1*0 + -2*1 + -3*2 + -4*3 + -5*4)

def test_calculate_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    test_list = [10, -5, 3, -2, 7]
    assert calculate_sum(test_list) == (10*0 + -5*1 + 3*2 + -2*3 + 7*4)

def test_calculate_sum_zero_list():
    """Test with a list of zeros"""
    test_list = [0, 0, 0, 0]
    assert calculate_sum(test_list) == 0