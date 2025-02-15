import pytest
from src.lcm import calculate_lcm

def test_lcm_basic_numbers():
    """Test LCM of basic positive numbers"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(15, 25) == 75
    assert calculate_lcm(12, 18) == 36

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert calculate_lcm(7, 7) == 7

def test_lcm_one_number_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert calculate_lcm(5, 10) == 10
    assert calculate_lcm(8, 16) == 16

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers"""
    assert calculate_lcm(17, 23) == 391

def test_lcm_invalid_inputs():
    """Test that invalid inputs raise ValueError"""
    with pytest.raises(ValueError):
        calculate_lcm(0, 5)
    with pytest.raises(ValueError):
        calculate_lcm(5, 0)
    with pytest.raises(ValueError):
        calculate_lcm(-4, 6)
    with pytest.raises(ValueError):
        calculate_lcm(4, -6)