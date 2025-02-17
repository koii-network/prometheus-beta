import pytest
from src.bitwise_and_range import bitwise_and_range

def test_bitwise_and_range_basic():
    """Test basic bitwise AND of range"""
    assert bitwise_and_range(1, 3) == 1  # 1 & 2 & 3 = 1
    assert bitwise_and_range(4, 7) == 4  # 4 & 5 & 6 & 7 = 4

def test_bitwise_and_range_single_number():
    """Test when start and end are the same"""
    assert bitwise_and_range(5, 5) == 5

def test_bitwise_and_range_zero():
    """Test range starting from zero"""
    assert bitwise_and_range(0, 3) == 0

def test_bitwise_and_range_larger_numbers():
    """Test with larger range of numbers"""
    assert bitwise_and_range(10, 14) == 10

def test_bitwise_and_range_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Start and end must be non-negative integers"):
        bitwise_and_range(-1, 5)
    
    with pytest.raises(ValueError, match="Start and end must be non-negative integers"):
        bitwise_and_range(1, -5)
    
    with pytest.raises(ValueError, match="Start must be less than or equal to end"):
        bitwise_and_range(10, 5)