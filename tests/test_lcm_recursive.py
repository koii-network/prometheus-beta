import pytest
from src.lcm_recursive import lcm_recursive, gcd_recursive

def test_gcd_recursive():
    """Test the recursive GCD function."""
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(17, 23) == 1
    assert gcd_recursive(0, 5) == 5
    assert gcd_recursive(5, 0) == 5

def test_lcm_recursive():
    """Test the recursive LCM function."""
    assert lcm_recursive(4, 6) == 12
    assert lcm_recursive(21, 6) == 42
    assert lcm_recursive(17, 23) == 391
    assert lcm_recursive(48, 18) == 144

def test_lcm_recursive_same_number():
    """Test LCM when both numbers are the same."""
    assert lcm_recursive(7, 7) == 7

def test_lcm_recursive_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        lcm_recursive(3.14, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm_recursive(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm_recursive(-3, 5)