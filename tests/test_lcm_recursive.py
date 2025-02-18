import pytest
from src.lcm_recursive import lcm_recursive, gcd_recursive

def test_gcd_recursive():
    """Test the helper GCD recursive function."""
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(17, 23) == 1

def test_lcm_recursive_basic():
    """Test basic LCM calculations."""
    assert lcm_recursive(4, 6) == 12
    assert lcm_recursive(21, 6) == 42
    assert lcm_recursive(17, 23) == 391

def test_lcm_recursive_same_number():
    """Test LCM when numbers are the same."""
    assert lcm_recursive(5, 5) == 5
    assert lcm_recursive(10, 10) == 10

def test_lcm_recursive_one_is_multiple():
    """Test LCM where one number is a multiple of the other."""
    assert lcm_recursive(3, 9) == 9
    assert lcm_recursive(7, 14) == 14

def test_lcm_recursive_coprime():
    """Test LCM for coprime numbers."""
    assert lcm_recursive(7, 11) == 77
    assert lcm_recursive(13, 17) == 221

def test_lcm_recursive_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        lcm_recursive(4.5, 6)
    
    with pytest.raises(TypeError):
        lcm_recursive("4", 6)
    
    with pytest.raises(ValueError):
        lcm_recursive(0, 6)
    
    with pytest.raises(ValueError):
        lcm_recursive(4, -6)
    
    with pytest.raises(ValueError):
        lcm_recursive(-4, 6)