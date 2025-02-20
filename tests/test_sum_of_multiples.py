import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_range():
    """Test a basic range with multiple multiples of 2 and 3"""
    assert sum_of_multiples(1, 10) == 33  # 2+3+4+6+8+9+10 = 33

def test_minimum_max_same():
    """Test when min and max are the same number"""
    assert sum_of_multiples(6, 6) == 6  # 6 is divisible by both 2 and 3
    assert sum_of_multiples(5, 5) == 0  # 5 is not divisible by 2 or 3

def test_large_range():
    """Test a larger range"""
    assert sum_of_multiples(1, 20) == 78  # sum of 2,3,4,6,8,9,10,12,14,15,16,18,20

def test_min_greater_than_max():
    """Test that an error is raised when min > max"""
    with pytest.raises(ValueError, match="min must be less than or equal to max"):
        sum_of_multiples(10, 5)

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Both min and max must be integers"):
        sum_of_multiples(1.5, 10)
    with pytest.raises(TypeError, match="Both min and max must be integers"):
        sum_of_multiples("1", 10)

def test_zero_range():
    """Test a range starting from 0"""
    assert sum_of_multiples(0, 10) == 33  # includes 0 which is divisible by 2