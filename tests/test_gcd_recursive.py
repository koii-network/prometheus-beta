import pytest
from src.gcd_recursive import gcd

def test_gcd_basic_cases():
    """Test basic GCD scenarios"""
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(17, 23) == 1
    assert gcd(100, 75) == 25

def test_gcd_zero_cases():
    """Test cases involving zero"""
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

def test_gcd_same_number():
    """Test when both numbers are the same"""
    assert gcd(7, 7) == 7
    assert gcd(13, 13) == 13

def test_gcd_negative_input():
    """Test error handling for negative inputs"""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        gcd(-10, 20)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        gcd(10, -20)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        gcd(-10, -20)