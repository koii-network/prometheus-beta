import pytest
from src.gcd import recursive_gcd

def test_recursive_gcd_basic():
    """Test basic GCD calculations"""
    assert recursive_gcd(48, 18) == 6
    assert recursive_gcd(54, 24) == 6
    assert recursive_gcd(17, 23) == 1

def test_recursive_gcd_zero():
    """Test cases involving zero"""
    assert recursive_gcd(0, 5) == 5
    assert recursive_gcd(5, 0) == 5
    assert recursive_gcd(0, 0) == 0

def test_recursive_gcd_negative():
    """Test cases with negative numbers"""
    assert recursive_gcd(-48, 18) == 6
    assert recursive_gcd(48, -18) == 6
    assert recursive_gcd(-48, -18) == 6

def test_recursive_gcd_same_number():
    """Test cases where both numbers are the same"""
    assert recursive_gcd(7, 7) == 7
    assert recursive_gcd(100, 100) == 100

def test_recursive_gcd_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        recursive_gcd(3.5, 7)
    with pytest.raises(ValueError):
        recursive_gcd("10", 20)
    with pytest.raises(ValueError):
        recursive_gcd([1], 20)