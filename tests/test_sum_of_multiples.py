import pytest
from src.sum_of_multiples import sum_of_multiples

def test_sum_of_multiples_basic():
    """Test basic functionality with a simple range"""
    assert sum_of_multiples(1, 10) == 33  # 2+3+4+6+8+9+10 = 33

def test_sum_of_multiples_small_range():
    """Test with a very small range"""
    assert sum_of_multiples(1, 3) == 5  # 2+3 = 5

def test_sum_of_multiples_zero_range():
    """Test with a range starting at zero"""
    assert sum_of_multiples(0, 5) == 15  # 0+2+3+4+6 = 15

def test_sum_of_multiples_same_number():
    """Test when min and max are the same number"""
    assert sum_of_multiples(3, 3) == 3  # 3 is a multiple of 3
    assert sum_of_multiples(2, 2) == 2  # 2 is a multiple of 2
    assert sum_of_multiples(5, 5) == 0  # 5 is not a multiple of 2 or 3

def test_sum_of_multiples_large_range():
    """Test with a larger range"""
    assert sum_of_multiples(1, 20) == 78  # Sum of multiples in this range

def test_sum_of_multiples_reverse_range():
    """Test when min is greater than max"""
    assert sum_of_multiples(10, 5) == 0  # Invalid range

def test_sum_of_multiples_negative_numbers():
    """Test with negative numbers in the range"""
    assert sum_of_multiples(-5, 5) == 15  # -4-3-2+0+2+3+4+6 = 15