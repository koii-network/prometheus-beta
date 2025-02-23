import pytest
from src.bitwise_range_and import bitwise_and_range

def test_bitwise_and_range_basic():
    """Test basic functionality of bitwise AND range"""
    assert bitwise_and_range(5, 7) == 4

def test_bitwise_and_range_same_number():
    """Test when start and end are the same number"""
    assert bitwise_and_range(10, 10) == 10

def test_bitwise_and_range_zero():
    """Test range starting from zero"""
    assert bitwise_and_range(0, 5) == 0

def test_bitwise_and_range_larger_range():
    """Test a larger range of numbers"""
    assert bitwise_and_range(12, 15) == 12

def test_bitwise_and_range_negative_start_raises_error():
    """Test that negative start raises ValueError"""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        bitwise_and_range(-1, 5)

def test_bitwise_and_range_negative_end_raises_error():
    """Test that negative end raises ValueError"""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        bitwise_and_range(1, -5)

def test_bitwise_and_range_start_greater_than_end_raises_error():
    """Test that start > end raises ValueError"""
    with pytest.raises(ValueError, match="Start must be less than or equal to end"):
        bitwise_and_range(10, 5)

def test_bitwise_and_range_large_numbers():
    """Test with larger numbers to ensure correct bitwise AND"""
    assert bitwise_and_range(1000, 1005) == 1000