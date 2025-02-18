import pytest
from src.euclidean_gcd import gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(17, 23) == 1
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5

def test_gcd_same_numbers():
    """Test GCD when both numbers are the same"""
    assert gcd(7, 7) == 7
    assert gcd(100, 100) == 100

def test_gcd_one_number_zero():
    """Test GCD when one number is zero"""
    assert gcd(0, 0) == 0
    assert gcd(5, 0) == 5
    assert gcd(0, 5) == 5

def test_gcd_coprime():
    """Test GCD of coprime numbers"""
    assert gcd(17, 23) == 1
    assert gcd(13, 17) == 1

def test_gcd_negative_input():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError):
        gcd(-5, 10)
    with pytest.raises(ValueError):
        gcd(5, -10)
    with pytest.raises(ValueError):
        gcd(-5, -10)

def test_gcd_large_numbers():
    """Test GCD with larger numbers"""
    assert gcd(1071, 462) == 21
    assert gcd(462, 1071) == 21  # Order shouldn't matter
    assert gcd(123456, 789012) == 12