import pytest
from src.lcm_calculator import calculate_lcm

def test_lcm_basic_numbers():
    """Test LCM calculation for basic positive integers"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(3, 5) == 15
    assert calculate_lcm(2, 7) == 14

def test_lcm_same_number():
    """Test LCM when both inputs are the same"""
    assert calculate_lcm(5, 5) == 5
    assert calculate_lcm(10, 10) == 10

def test_lcm_one_number_multiple_of_other():
    """Test LCM when one number is a multiple of the other"""
    assert calculate_lcm(4, 8) == 8
    assert calculate_lcm(7, 14) == 14

def test_lcm_coprime_numbers():
    """Test LCM for coprime numbers"""
    assert calculate_lcm(7, 11) == 77
    assert calculate_lcm(13, 17) == 221

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(-3, 7)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(5, -2)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(0, 0)