import pytest
from src.lcm_recursive import lcm_recursive, gcd_recursive

def test_lcm_recursive_basic():
    """Test basic LCM calculations"""
    assert lcm_recursive(4, 6) == 12
    assert lcm_recursive(21, 6) == 42
    assert lcm_recursive(17, 5) == 85

def test_lcm_recursive_negative_numbers():
    """Test LCM with negative numbers"""
    assert lcm_recursive(-4, 6) == 12
    assert lcm_recursive(4, -6) == 12
    assert lcm_recursive(-4, -6) == 12

def test_lcm_recursive_prime_numbers():
    """Test LCM of prime numbers"""
    assert lcm_recursive(7, 11) == 77
    assert lcm_recursive(13, 17) == 221

def test_lcm_recursive_one_number():
    """Test LCM when one number is 1"""
    assert lcm_recursive(1, 5) == 5
    assert lcm_recursive(5, 1) == 5

def test_lcm_recursive_same_numbers():
    """Test LCM of the same number"""
    assert lcm_recursive(7, 7) == 7
    assert lcm_recursive(-7, -7) == 7

def test_lcm_recursive_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        lcm_recursive(4.5, 6)
    with pytest.raises(TypeError):
        lcm_recursive(4, '6')
    with pytest.raises(TypeError):
        lcm_recursive('4', 6)

def test_lcm_recursive_zero():
    """Test error handling for zero input"""
    with pytest.raises(ValueError):
        lcm_recursive(0, 5)
    with pytest.raises(ValueError):
        lcm_recursive(5, 0)

def test_gcd_recursive_basic():
    """Test the internal GCD recursive function"""
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(17, 23) == 1  # prime numbers
    assert gcd_recursive(-48, 18) == 6  # negative numbers