import pytest
from src.gcd import find_gcd

def test_gcd_positive_numbers():
    """Test GCD for positive numbers"""
    assert find_gcd(48, 18) == 6
    assert find_gcd(54, 24) == 6
    assert find_gcd(17, 23) == 1  # coprime numbers

def test_gcd_zero_inputs():
    """Test GCD with zero inputs"""
    assert find_gcd(0, 5) == 5
    assert find_gcd(5, 0) == 5
    assert find_gcd(0, 0) == 0

def test_gcd_negative_numbers():
    """Test GCD with negative numbers"""
    assert find_gcd(-48, 18) == 6
    assert find_gcd(48, -18) == 6
    assert find_gcd(-48, -18) == 6

def test_gcd_invalid_inputs():
    """Test GCD with invalid input types"""
    with pytest.raises(ValueError):
        find_gcd(3.14, 5)
    with pytest.raises(ValueError):
        find_gcd("10", 5)
    with pytest.raises(ValueError):
        find_gcd([10], 5)