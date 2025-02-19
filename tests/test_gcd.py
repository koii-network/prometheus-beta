import pytest
from src.gcd import calculate_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert calculate_gcd(48, 18) == 6
    assert calculate_gcd(54, 24) == 6
    assert calculate_gcd(17, 23) == 1
    assert calculate_gcd(100, 75) == 25

def test_gcd_same_number():
    """Test GCD when both numbers are the same"""
    assert calculate_gcd(7, 7) == 7
    assert calculate_gcd(100, 100) == 100

def test_gcd_one_is_multiple():
    """Test GCD when one number is a multiple of the other"""
    assert calculate_gcd(12, 3) == 3
    assert calculate_gcd(17, 1) == 1

def test_gcd_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_gcd(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_gcd(5, 0)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_gcd(-5, 10)
    
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_gcd(5.5, 10)
    
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_gcd("5", 10)