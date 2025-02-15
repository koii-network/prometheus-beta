import pytest
from src.gcd import gcd

def test_gcd_positive_numbers():
    """Test GCD of positive numbers"""
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(17, 23) == 1

def test_gcd_zero_case():
    """Test GCD when one number is zero"""
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

def test_gcd_negative_numbers():
    """Test GCD with negative numbers"""
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6

def test_gcd_same_numbers():
    """Test GCD of the same number"""
    assert gcd(7, 7) == 7
    assert gcd(100, 100) == 100

def test_gcd_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        gcd(3.14, 5)
    with pytest.raises(ValueError):
        gcd("10", 5)
    with pytest.raises(ValueError):
        gcd([], 5)