import pytest
from src.bitwise_and_range import bitwise_and_range

def test_bitwise_and_range_basic():
    # Simple range test
    assert bitwise_and_range(5, 7) == 4

def test_bitwise_and_range_single_number():
    # Test when start and end are the same
    assert bitwise_and_range(10, 10) == 10

def test_bitwise_and_range_zero():
    # Test with zero in range
    assert bitwise_and_range(0, 5) == 0

def test_bitwise_and_range_large_numbers():
    # Test with larger numbers
    assert bitwise_and_range(12, 15) == 12

def test_bitwise_and_range_negative_input():
    # Test negative input raises ValueError
    with pytest.raises(ValueError, match="Start and end must be non-negative integers"):
        bitwise_and_range(-1, 5)
    with pytest.raises(ValueError, match="Start and end must be non-negative integers"):
        bitwise_and_range(5, -1)

def test_bitwise_and_range_invalid_range():
    # Test when start is greater than end
    with pytest.raises(ValueError, match="Start must be less than or equal to end"):
        bitwise_and_range(10, 5)