import pytest
from src.lcm import find_lcm

def test_lcm_basic_numbers():
    """Test LCM for basic positive numbers"""
    assert find_lcm(4, 6) == 12
    assert find_lcm(21, 6) == 42
    assert find_lcm(17, 5) == 85

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert find_lcm(7, 7) == 7
    assert find_lcm(13, 13) == 13

def test_lcm_one_number_is_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert find_lcm(8, 4) == 8
    assert find_lcm(15, 5) == 15

def test_lcm_coprime_numbers():
    """Test LCM for coprime numbers"""
    assert find_lcm(17, 23) == 391

def test_lcm_invalid_input():
    """Test that ValueError is raised for non-positive inputs"""
    with pytest.raises(ValueError, match="Both numbers must be positive integers"):
        find_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Both numbers must be positive integers"):
        find_lcm(-3, 7)
    
    with pytest.raises(ValueError, match="Both numbers must be positive integers"):
        find_lcm(4, -2)