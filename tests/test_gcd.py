import pytest
from src.gcd import find_gcd

def test_gcd_normal_cases():
    """Test GCD for normal positive integers"""
    assert find_gcd(48, 18) == 6
    assert find_gcd(54, 24) == 6
    assert find_gcd(17, 23) == 1

def test_gcd_large_numbers():
    """Test GCD for large numbers"""
    assert find_gcd(1071, 462) == 21
    assert find_gcd(123456, 789) == 3

def test_gcd_same_number():
    """Test GCD when both numbers are the same"""
    assert find_gcd(5, 5) == 5
    assert find_gcd(100, 100) == 100

def test_gcd_one_is_multiple_of_other():
    """Test GCD when one number is a multiple of the other"""
    assert find_gcd(10, 5) == 5
    assert find_gcd(7, 14) == 7

def test_gcd_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_gcd(3.14, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_gcd(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_gcd(-5, 10)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_gcd(-3, -7)