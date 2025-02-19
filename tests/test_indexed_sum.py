import pytest
from src.indexed_sum import calculate_sum

def test_calculate_sum_normal_case():
    """Test with a normal list of integers"""
    test_list = [1, 2, 3, 4, 5]
    assert calculate_sum(test_list) == 40  # 0*1 + 1*2 + 2*3 + 3*4 + 4*5 = 40

def test_calculate_sum_empty_list():
    """Test with an empty list"""
    assert calculate_sum([]) == 0

def test_calculate_sum_negative_numbers():
    """Test with a list containing negative numbers"""
    test_list = [-1, -2, -3, -4, -5]
    assert calculate_sum(test_list) == -40  # 0*(-1) + 1*(-2) + 2*(-3) + 3*(-4) + 4*(-5) = -40

def test_calculate_sum_mixed_numbers():
    """Test with a list containing mixed positive and negative numbers"""
    test_list = [1, -2, 3, -4, 5]
    assert calculate_sum(test_list) == 10  # 0*1 + 1*(-2) + 2*3 + 3*(-4) + 4*5 = 10

def test_calculate_sum_invalid_input():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")
        calculate_sum(123)
        calculate_sum(None)