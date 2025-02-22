import pytest
from src.gcd import find_gcd

def test_gcd_basic_cases():
    """Test basic GCD scenarios"""
    assert find_gcd(48, 18) == 6
    assert find_gcd(54, 24) == 6
    assert find_gcd(17, 23) == 1
    assert find_gcd(100, 75) == 25

def test_gcd_same_number():
    """Test when both numbers are the same"""
    assert find_gcd(7, 7) == 7
    assert find_gcd(13, 13) == 13

def test_gcd_coprime():
    """Test coprime numbers"""
    assert find_gcd(17, 23) == 1
    assert find_gcd(11, 13) == 1

def test_gcd_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_gcd(10.5, 20)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_gcd(0, 10)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_gcd(-5, 10)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_gcd(10, 0)