import pytest
from src.calculate_sum import calculate_sum

def test_calculate_sum_normal_case():
    """Test normal case with various integers"""
    assert calculate_sum([1, 2, 3, 4]) == 20  # 0*1 + 1*2 + 2*3 + 3*4 = 0 + 2 + 6 + 12 = 20

def test_calculate_sum_empty_list():
    """Test with an empty list"""
    assert calculate_sum([]) == 0

def test_calculate_sum_negative_numbers():
    """Test with negative numbers"""
    assert calculate_sum([-1, -2, -3]) == -8  # 0*(-1) + 1*(-2) + 2*(-3) = 0 - 2 - 6 = -8

def test_calculate_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert calculate_sum([1, -2, 3, -4]) == -8  # 0*1 + 1*(-2) + 2*3 + 3*(-4) = 0 - 2 + 6 - 12 = -8

def test_calculate_sum_invalid_type():
    """Test with invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")

def test_calculate_sum_non_integer_elements():
    """Test with non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        calculate_sum([1, 2, "3", 4])