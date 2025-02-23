import pytest
from src.gcd import gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(17, 23) == 1
    assert gcd(48, 180) == 12

def test_gcd_zero_cases():
    """Test cases involving zero"""
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

def test_gcd_negative_inputs():
    """Test handling of negative inputs"""
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6

def test_gcd_same_number():
    """Test GCD of the same number"""
    assert gcd(7, 7) == 7
    assert gcd(42, 42) == 42

def test_gcd_one_cases():
    """Test cases with one as input"""
    assert gcd(1, 5) == 1
    assert gcd(5, 1) == 1

def test_gcd_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        gcd(3.14, 5)
    with pytest.raises(ValueError):
        gcd(5, '10')
    with pytest.raises(ValueError):
        gcd('10', 5)