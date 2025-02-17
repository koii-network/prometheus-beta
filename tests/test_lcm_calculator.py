import pytest
from src.lcm_calculator import calculate_lcm

def test_lcm_positive_numbers():
    """Test LCM calculation for regular positive numbers"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(21, 6) == 42
    assert calculate_lcm(17, 23) == 391

def test_lcm_same_number():
    """Test when both numbers are the same"""
    assert calculate_lcm(5, 5) == 5
    assert calculate_lcm(100, 100) == 100

def test_lcm_one_multiple_of_other():
    """Test when one number is a multiple of the other"""
    assert calculate_lcm(3, 9) == 9
    assert calculate_lcm(8, 16) == 16

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers"""
    assert calculate_lcm(7, 13) == 91

def test_lcm_invalid_input():
    """Test that invalid inputs raise ValueError"""
    with pytest.raises(ValueError):
        calculate_lcm(0, 5)
    with pytest.raises(ValueError):
        calculate_lcm(5, 0)
    with pytest.raises(ValueError):
        calculate_lcm(-3, 5)
    with pytest.raises(ValueError):
        calculate_lcm(3, -5)