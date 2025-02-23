import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_range():
    """Test a basic range of numbers"""
    assert sum_of_multiples(1, 10) == 33  # 2 + 3 + 4 + 6 + 8 + 9 + 10

def test_range_with_start_greater_than_multiples():
    """Test a range where start is greater than some multiples"""
    assert sum_of_multiples(5, 10) == 18  # 6 + 8 + 9 + 10

def test_single_number_range():
    """Test a range with a single number"""
    assert sum_of_multiples(6, 6) == 6  # just 6
    assert sum_of_multiples(7, 7) == 0  # no multiple of 2 or 3

def test_larger_range():
    """Test a larger range of numbers"""
    assert sum_of_multiples(1, 20) == 78  # sum of multiples 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20

def test_invalid_range():
    """Test when min is greater than max"""
    assert sum_of_multiples(10, 5) == 0

def test_zero_range():
    """Test range starting and ending at zero"""
    assert sum_of_multiples(0, 0) == 0