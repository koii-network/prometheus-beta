import pytest
from src.lcm_calculator import calculate_lcm

def test_lcm_basic_numbers():
    """Test LCM of basic integer numbers"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(15, 25) == 75
    assert calculate_lcm(12, 18) == 36

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert calculate_lcm(7, 7) == 7

def test_lcm_one_number_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert calculate_lcm(10, 5) == 10
    assert calculate_lcm(5, 10) == 10

def test_lcm_large_numbers():
    """Test LCM with larger numbers"""
    assert calculate_lcm(48, 180) == 720

def test_lcm_invalid_input():
    """Test LCM with invalid inputs"""
    with pytest.raises(ValueError, match="Both numbers must be positive integers"):
        calculate_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Both numbers must be positive integers"):
        calculate_lcm(-3, 7)
    
    with pytest.raises(ValueError, match="Both numbers must be positive integers"):
        calculate_lcm(5, -3)