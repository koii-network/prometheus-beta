import pytest
from src.lcm_recursive import lcm_recursive, gcd_recursive

def test_gcd_recursive():
    """Test the Greatest Common Divisor recursive function."""
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(17, 23) == 1
    assert gcd_recursive(100, 75) == 25

def test_lcm_recursive_basic():
    """Test basic LCM calculations."""
    assert lcm_recursive(4, 6) == 12
    assert lcm_recursive(21, 6) == 42
    assert lcm_recursive(17, 23) == 391

def test_lcm_recursive_same_number():
    """Test LCM when both numbers are the same."""
    assert lcm_recursive(5, 5) == 5
    assert lcm_recursive(7, 7) == 7

def test_lcm_recursive_coprime():
    """Test LCM for coprime numbers."""
    assert lcm_recursive(7, 11) == 77
    assert lcm_recursive(13, 17) == 221

def test_lcm_recursive_invalid_input():
    """Test handling of invalid inputs."""
    with pytest.raises(ValueError, match="Both numbers must be positive integers"):
        lcm_recursive(0, 5)
    with pytest.raises(ValueError, match="Both numbers must be positive integers"):
        lcm_recursive(-3, 10)
    with pytest.raises(ValueError, match="Both numbers must be positive integers"):
        lcm_recursive(5, -7)