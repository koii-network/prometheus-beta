import pytest
from src.weighted_sum import calculate_sum

def test_calculate_sum_normal_case():
    """Test with a normal list of integers"""
    test_list = [1, 2, 3, 4, 5]
    # Expected calculation: 
    # 1*0 + 2*1 + 3*2 + 4*3 + 5*4 = 0 + 2 + 6 + 12 + 20 = 40
    assert calculate_sum(test_list) == 40

def test_calculate_sum_empty_list():
    """Test with an empty list"""
    assert calculate_sum([]) == 0

def test_calculate_sum_single_element():
    """Test with a single element list"""
    assert calculate_sum([10]) == 0

def test_calculate_sum_negative_numbers():
    """Test with negative numbers"""
    test_list = [-1, -2, -3, -4, -5]
    # Expected calculation:
    # -1*0 + -2*1 + -3*2 + -4*3 + -5*4 = 0 - 2 - 6 - 12 - 20 = -40
    assert calculate_sum(test_list) == -40

def test_calculate_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    test_list = [-1, 2, -3, 4, -5]
    # Expected calculation:
    # -1*0 + 2*1 + -3*2 + 4*3 + -5*4 = 0 + 2 - 6 + 12 - 20 = -12
    assert calculate_sum(test_list) == -12