import pytest
from src.bitwise_and_range import bitwise_and_range

def test_bitwise_and_range_same_number():
    """Test when start and end are the same number"""
    assert bitwise_and_range(5, 5) == 5

def test_bitwise_and_range_simple_case():
    """Test a simple range with bitwise AND"""
    assert bitwise_and_range(5, 7) == 4

def test_bitwise_and_range_zero():
    """Test range starting from zero"""
    assert bitwise_and_range(0, 5) == 0

def test_bitwise_and_range_larger_numbers():
    """Test with larger numbers"""
    assert bitwise_and_range(10, 15) == 8

def test_bitwise_and_range_negative_input():
    """Test that negative inputs raise ValueError"""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        bitwise_and_range(-1, 5)
    
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        bitwise_and_range(5, -1)

def test_bitwise_and_range_invalid_range():
    """Test that start > end raises ValueError"""
    with pytest.raises(ValueError, match="Start must be less than or equal to end"):
        bitwise_and_range(10, 5)

def test_bitwise_and_range_consecutive_numbers():
    """Test with consecutive numbers"""
    assert bitwise_and_range(128, 135) == 128