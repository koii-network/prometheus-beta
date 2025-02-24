import pytest
from src.gcd import find_gcd

def test_gcd_positive_numbers():
    """Test GCD of positive numbers"""
    assert find_gcd(48, 18) == 6
    assert find_gcd(54, 24) == 6
    assert find_gcd(17, 23) == 1

def test_gcd_zero_cases():
    """Test GCD with zero inputs"""
    assert find_gcd(0, 5) == 5
    assert find_gcd(5, 0) == 5
    assert find_gcd(0, 0) == 0

def test_gcd_same_number():
    """Test GCD of same number"""
    assert find_gcd(7, 7) == 7

def test_gcd_one_number():
    """Test GCD when one number is 1"""
    assert find_gcd(1, 5) == 1
    assert find_gcd(5, 1) == 1

def test_gcd_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_gcd("48", 18)
    
    with pytest.raises(TypeError):
        find_gcd(48, "18")
    
    with pytest.raises(TypeError):
        find_gcd(4.8, 18)

def test_gcd_negative_inputs():
    """Test error handling for negative inputs"""
    with pytest.raises(ValueError):
        find_gcd(-48, 18)
    
    with pytest.raises(ValueError):
        find_gcd(48, -18)