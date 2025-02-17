import pytest
from src.bitwise_and_range import bitwise_and_range

def test_bitwise_and_range_normal_case():
    # Test a typical range
    assert bitwise_and_range(5, 7) == 4  # Binary: 101 & 110 & 111 = 100 (4)

def test_bitwise_and_range_single_number():
    # Test when start and end are the same
    assert bitwise_and_range(10, 10) == 10

def test_bitwise_and_range_zero_case():
    # Test case with zero
    assert bitwise_and_range(0, 3) == 0

def test_bitwise_and_range_negative_error():
    # Test start > end scenario
    with pytest.raises(ValueError):
        bitwise_and_range(10, 5)

def test_bitwise_and_range_type_error():
    # Test non-integer inputs
    with pytest.raises(TypeError):
        bitwise_and_range(5.5, 7)
    
    with pytest.raises(TypeError):
        bitwise_and_range(5, '7')

def test_bitwise_and_range_large_numbers():
    # Test a larger range
    assert bitwise_and_range(1000, 1005) == 1000