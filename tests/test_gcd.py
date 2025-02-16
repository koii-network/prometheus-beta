import pytest
from src.gcd import find_gcd

def test_gcd_positive_numbers():
    """Test GCD of positive numbers"""
    assert find_gcd(48, 18) == 6
    assert find_gcd(54, 24) == 6
    assert find_gcd(17, 23) == 1

def test_gcd_one_zero():
    """Test GCD when one number is zero"""
    assert find_gcd(0, 5) == 5
    assert find_gcd(5, 0) == 5

def test_gcd_same_numbers():
    """Test GCD of same numbers"""
    assert find_gcd(7, 7) == 7

def test_gcd_negative_numbers():
    """Test GCD with negative numbers"""
    assert find_gcd(-48, 18) == 6
    assert find_gcd(48, -18) == 6
    assert find_gcd(-48, -18) == 6

def test_gcd_invalid_inputs():
    """Test invalid input types"""
    with pytest.raises(ValueError):
        find_gcd(3.5, 4)
    with pytest.raises(ValueError):
        find_gcd("10", 4)
    with pytest.raises(ValueError):
        find_gcd([10], 4)