import pytest
from src.lcm_calculator import calculate_lcm

def test_lcm_basic_cases():
    """Test basic LCM calculations"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(15, 25) == 75
    assert calculate_lcm(8, 12) == 24

def test_lcm_one_is_multiple():
    """Test when one number is a multiple of the other"""
    assert calculate_lcm(5, 10) == 10
    assert calculate_lcm(7, 14) == 14

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers"""
    assert calculate_lcm(7, 11) == 77
    assert calculate_lcm(13, 17) == 221

def test_lcm_same_number():
    """Test LCM of the same number"""
    assert calculate_lcm(5, 5) == 5
    assert calculate_lcm(100, 100) == 100

def test_lcm_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(-3, 7)
    
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_lcm(3.5, 7)
    
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_lcm("5", 7)