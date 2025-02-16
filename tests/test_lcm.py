import pytest
from src.lcm import calculate_lcm

def test_lcm_positive_numbers():
    """Test LCM of various positive number combinations"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(21, 6) == 42
    assert calculate_lcm(17, 5) == 85

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert calculate_lcm(7, 7) == 7
    assert calculate_lcm(13, 13) == 13

def test_lcm_one_number_is_one():
    """Test LCM when one number is 1"""
    assert calculate_lcm(1, 5) == 5
    assert calculate_lcm(5, 1) == 5

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers"""
    assert calculate_lcm(7, 11) == 77
    assert calculate_lcm(13, 17) == 221

def test_invalid_input():
    """Test handling of invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(0, 5)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(-3, 4)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(5, 0)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(5, -7)