import pytest
from src.gcd import recursive_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert recursive_gcd(48, 18) == 6
    assert recursive_gcd(54, 24) == 6
    assert recursive_gcd(17, 5) == 1

def test_gcd_zero_cases():
    """Test GCD with zero"""
    assert recursive_gcd(0, 5) == 5
    assert recursive_gcd(5, 0) == 5
    assert recursive_gcd(0, 0) == 0

def test_gcd_same_number():
    """Test GCD when both numbers are the same"""
    assert recursive_gcd(7, 7) == 7
    assert recursive_gcd(13, 13) == 13

def test_gcd_one_number():
    """Test GCD when one number is 1"""
    assert recursive_gcd(1, 5) == 1
    assert recursive_gcd(5, 1) == 1

def test_gcd_negative_input():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        recursive_gcd(-5, 10)
    
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        recursive_gcd(10, -5)
    
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        recursive_gcd(-5, -10)

def test_large_numbers():
    """Test GCD with larger numbers"""
    assert recursive_gcd(1071, 462) == 21
    assert recursive_gcd(123456, 987654) == 6