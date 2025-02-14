import pytest
from src.lcm import calculate_lcm

def test_lcm_positive_numbers():
    """Test LCM of positive integers"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(21, 6) == 42
    assert calculate_lcm(17, 5) == 85

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert calculate_lcm(7, 7) == 7

def test_lcm_one_number_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert calculate_lcm(8, 4) == 8
    assert calculate_lcm(15, 5) == 15

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers"""
    assert calculate_lcm(13, 17) == 221

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_lcm(3.5, 4)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(-3, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(5, -3)