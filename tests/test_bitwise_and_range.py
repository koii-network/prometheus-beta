import pytest
from src.bitwise_and_range import bitwise_and_range

def test_bitwise_and_range_single_number():
    """Test bitwise AND for a single number"""
    assert bitwise_and_range(5, 5) == 5

def test_bitwise_and_range_same_prefix():
    """Test bitwise AND for range with same prefix"""
    assert bitwise_and_range(5, 7) == 4

def test_bitwise_and_range_different_prefixes():
    """Test bitwise AND for range with different prefixes"""
    assert bitwise_and_range(10, 15) == 8

def test_bitwise_and_range_zero_range():
    """Test bitwise AND for 0 to 0"""
    assert bitwise_and_range(0, 0) == 0

def test_bitwise_and_range_invalid_start_greater_end():
    """Test raising ValueError when start is greater than end"""
    with pytest.raises(ValueError, match="Start must be less than or equal to end"):
        bitwise_and_range(10, 5)

def test_bitwise_and_range_negative_inputs():
    """Test raising ValueError for negative inputs"""
    with pytest.raises(ValueError, match="Start and end must be non-negative integers"):
        bitwise_and_range(-1, 5)
    with pytest.raises(ValueError, match="Start and end must be non-negative integers"):
        bitwise_and_range(5, -1)

def test_bitwise_and_range_larger_numbers():
    """Test bitwise AND for larger numbers"""
    assert bitwise_and_range(1000, 1050) == 1024