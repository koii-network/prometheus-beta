import pytest
from src.bitwise_and_range import bitwise_and_range

def test_basic_range():
    """Test bitwise AND for a simple range of numbers"""
    assert bitwise_and_range(3, 5) == 1  # 3 & 4 & 5 = 1

def test_single_number_range():
    """Test bitwise AND when start and end are the same"""
    assert bitwise_and_range(7, 7) == 7

def test_zero_range():
    """Test bitwise AND with zero"""
    assert bitwise_and_range(0, 2) == 0

def test_larger_range():
    """Test bitwise AND with a larger range"""
    assert bitwise_and_range(10, 14) == 10

def test_invalid_range_start_gt_end():
    """Test that ValueError is raised when start > end"""
    with pytest.raises(ValueError, match="Start must be less than or equal to end"):
        bitwise_and_range(5, 3)

def test_negative_numbers():
    """Test that ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="Range numbers must be non-negative"):
        bitwise_and_range(-1, 5)
    with pytest.raises(ValueError, match="Range numbers must be non-negative"):
        bitwise_and_range(1, -5)