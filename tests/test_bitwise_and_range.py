import pytest
from src.bitwise_and_range import bitwise_and_range

def test_basic_range():
    """Test bitwise AND for a simple range"""
    assert bitwise_and_range(5, 7) == 4  # Binary: 101 & 110 & 111 = 100 (4)

def test_single_number():
    """Test bitwise AND when start and end are the same"""
    assert bitwise_and_range(10, 10) == 10

def test_zero_range():
    """Test bitwise AND for range starting at 0"""
    assert bitwise_and_range(0, 4) == 0

def test_large_range():
    """Test bitwise AND for a larger range"""
    assert bitwise_and_range(10, 15) == 10  # Binary: 1010 & 1011 & 1100 & 1101 & 1110 & 1111 = 1010 (10)

def test_invalid_negative_start():
    """Test that negative start raises ValueError"""
    with pytest.raises(ValueError, match="Both start and end must be non-negative integers"):
        bitwise_and_range(-1, 5)

def test_invalid_negative_end():
    """Test that negative end raises ValueError"""
    with pytest.raises(ValueError, match="Both start and end must be non-negative integers"):
        bitwise_and_range(1, -5)

def test_invalid_range():
    """Test that start > end raises ValueError"""
    with pytest.raises(ValueError, match="Start must be less than or equal to end"):
        bitwise_and_range(10, 5)