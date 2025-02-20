import pytest
from src.array_sum import sum_array

def test_sum_array_normal_case():
    """Test summing a normal array of positive integers"""
    assert sum_array([1, 2, 3, 4]) == 10

def test_sum_array_empty():
    """Test summing an empty array"""
    assert sum_array([]) == 0

def test_sum_array_negative_numbers():
    """Test summing an array with negative numbers"""
    assert sum_array([-1, -2, -3]) == -6

def test_sum_array_mixed_numbers():
    """Test summing an array with positive and negative numbers"""
    assert sum_array([-1, 0, 1]) == 0

def test_sum_array_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_array(123)

def test_sum_array_invalid_element_type():
    """Test raising TypeError for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_array([1, 2, '3', 4])